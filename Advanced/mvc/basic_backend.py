from mvc_exceptions import ItemAlreadyStored, ItemNotStored

items = list()


class Create(object):

    def all(self, app_items):
        global items
        items = app_items

    def item(self, **kwargs):
        try:
            global items
            name = kwargs.get('name')
            price = kwargs.get('price')
            quantity = kwargs.get('quantity')
            results = list(filter(lambda x: x['name'] == name, items))
            if len(results) == 0:
                items.append({
                    'name': name,
                    'price': price,
                    'quantity': quantity
                })
                return name
            raise ItemAlreadyStored('{msg} already stored!'.format(msg=name))
        except Exception as Error:
            raise ValueError(Error)


class Read(object):

    def all(self):
        global items
        return [item for item in items]

    def item(self, **kwargs):
        try:
            global items
            name = kwargs.get('name')
            myitems = list(filter(lambda x: x['name'] == name, items))
            if myitems:
                return myitems[0]
            raise ItemNotStored('Can not read {name} because its not stored.'.format(name=name))
        except Exception as Error:
            raise ValueError(Error)


class Update(object):

    def item(self, **kwargs):
        global items
        try:
            name = kwargs.get('name')
            price = kwargs.get('price')
            quantity = kwargs.get('quantity')
            idxs_items = list(filter(lambda i_x: i_x[1]['name'] == name, enumerate(items)))
            if idxs_items:
                i, item_to_update = idxs_items[0][0], idxs_items[0][1]
                items[i] = {
                    'name': name,
                    'price': price,
                    'quantity': quantity
                }
                return items[i]
            raise ItemNotStored('Can not update {item} because its not stored'.format(item=name))
        except Exception as Error:
            raise ValueError(Error)


class Delete(object):

    def item(self, **kwargs):
        global items
        try:
            name = kwargs.get('name')
            idxs_items = list(filter(lambda i_x: i_x[1]['name'] == name, enumerate(items)))
            if idxs_items:
                i, item_to_update = idxs_items[0][0], idxs_items_items[0][1]
                del items[i]
            raise ItemNotStored('Can not delete {item} because its not stored'.format(item=name))
        except Exception as Error:
            raise ValueError(Error)


class CrudOperation(object):

    def __init__(self):
        self.read = Read()
        self.create = Create()
        self.update = Update()
        self.delete = Delete()


def main():
    # INSTANCE CRUD OPERATION
    operation = CrudOperation()

    # GENERAL ITEM
    items = [
        {'name': 'bread', 'price': 0.5, 'quantity': 20},
        {'name': 'milk', 'price': 1.0, 'quantity': 10},
        {'name': 'wine', 'price': 10.0, 'quantity': 5},
    ]
    print(40 * '*')
    # CREATE
    operation.create.all(items)
    operation.create.item(name='beer', price=3.0, quantity=15)
    print(40*'*')
    # READ
    print('READ ALL ITEMS')
    print(operation.read.all())
    print('READ BREAD ITEM')
    print(operation.read.item(name='bread'))
    print(40 * '*')
    # UPDATE
    print('UPDATE BREAD')
    operation.update.item(name='bread', price=5.0, quantity=2)
    print(operation.read.item(name='bread'))


if __name__ == '__main__':
    main()
