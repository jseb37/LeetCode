store = {}
store['foo'] =[]
store['foo'].append(["bar",1])
store['foo'].append(["bar2",4])

print(store)
print(store.get('foo',[]))
print(store.get('hello',[]))
print(store.get('hello'))