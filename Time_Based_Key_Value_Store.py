'''
Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
String get(String key, int timestamp) Returns a value  with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".


Example 1:

Input
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
Output
[null, null, "bar", "bar", null, "bar2", "bar2"]

Explanation
TimeMap timeMap = new TimeMap();
timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
timeMap.get("foo", 1);         // return "bar"
timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
timeMap.get("foo", 4);         // return "bar2"
timeMap.get("foo", 5);         // return "bar2"

'''

#Explaination
store = {}
store['foo'] =[]
store['foo'].append(["bar",1])
store['foo'].append(["bar2",3])
store['foo'].append(["bar3",5])
store['foo'].append(["bar4",7])
store['foo'].append(["bar5",9])

print(store)
print(store.get('foo',[]))
print(store.get('hello',[]))
print(store.get('hello'))

 #1 3 5 7 9
 #If timestamp passed is 8,it gets bar4 corressponding to timestamp 7
 #If timestamp passed is 9,it gets bar5 corressponding to timestamp 9 - It is done using binary search



class TimeMap(object):

    def __init__(self):
        self.store = {} # key : list of [val, timestamp]


    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value ,timestamp])
    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        res = ""
        #dictionary.get(keyname, value)
        #keyname	Required. The keyname of the item you want to return the value from
        #value	Optional. A value to return if the specified key does not exist.
        #Default value None
        #Here if key doesnt exist return empty list or if exists return values corresponding to key
        values = self.store.get(key ,[])
        # binary search
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r ) // 2
            #If timestamp passed is not present in the list of list , return the 1st value in list of list corressponding to the previous highest
            # otherwise return the same 1st value in list of list corresponding to the timestamp
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
