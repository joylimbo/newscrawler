        #if self.db.tuan.find({"goodsid":item['goodsid'],"market":item['market']}).count() is 0:
        #    self.db.tuan.insert(dict(item))
        pass

    def process_store_item(self,item):
        print dict(item)
        #if self.db.store.find({"lon":item['lon'],"lat":item['lat']}).count() is 0:
        #    self.db.store.insert(dict(item))
        pass
