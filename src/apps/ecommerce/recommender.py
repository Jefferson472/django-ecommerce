import redis

from django.conf import settings

from .models import Product


# estabelecendo conexão com o redis
r = redis.Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    db=settings.REDIS_DB,
    password=settings.REDIS_PASSWORD,
)


class Recommender(object):
    def get_product_key(self, id):
        return f'product:{id}:purchased_with'

    def products_bought(self, products):
        product_ids = [p.id for p in products]
        for product_id in product_ids:
            for with_id in product_ids:
                # obtém os outros produtos comprados com cada produto
                if product_id != with_id:
                    # incrementa a pontuação dos produtos comprados juntos
                    r.zincrby(self.get_product_key(product_id), 1, with_id)
    
    def suggest_products_for(self, products, max_results=6):
        product_ids = [p.id for p in products]

        if len(products) == 1:
            # somente 1 produto
            suggestions = r.zrange(
                self.get_product_key(product_ids[0]),
                0, -1, desc=True
            )[:max_results]
        else:
            # gera uma chave temporária
            flat_ids = ''.join([str(id) for id in product_ids])
            temp_key = f'temp_{flat_ids}'
            # vários produtos; combina as pontuações de todos os produtos
            # armazena o conjunto ordenado resultante em uma chave temporária
            keys = [self.get_product_key(id) for id in product_ids]
            r.zunionstore(temp_key, keys)
            # remove os ids dos produtos para os quais a recomendação será feita
            r.zrem(temp_key, *product_ids)
            # obtém os ids dos produtos em ordem descrescente de suas pontuações
            suggestions = r.zrange(
                temp_key, 0, -1, desc=True, 
            )[:max_results]
            # remove a chave temporária
            r.delete(temp_key)
        suggested_products_ids = [int(id) for id in suggestions]

        # obtém os produtos sugeridos e ordena conforme a ordem em que aparecem
        suggested_products = list(Product.objects.filter(id__in=suggested_products_ids))
        suggested_products.sort(key=lambda x: suggested_products_ids.index(x.id))
        return suggested_products

    def clear_purchase(self):
        for id in Product.objects.values_list('id', flat=True):
            r.delete(self.get_product_key(id))