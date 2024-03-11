from collections import defaultdict

class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.freq_counter = defaultdict(int)
        self.freq_to_keys = defaultdict(list)
        self.min_freq = 0

    def get(self, key):
        if key in self.cache:
            # Increment frequency
            self.freq_counter[key] += 1
            freq = self.freq_counter[key]

            # Move key to the next frequency list
            self.freq_to_keys[freq].append(key)
            self.freq_to_keys[freq - 1].remove(key)

            # Update min_freq if necessary
            if not self.freq_to_keys[self.min_freq]:
                self.min_freq += 1

            return self.cache[key]
        else:
            return None

    def put(self, key, value):
        if self.capacity <= 0:
            return

        if key in self.cache:
            # If key exists, update value and frequency
            self.cache[key] = value
            self.get(key)  # Increment frequency as in the get method
        else:
            # Check capacity and evict if necessary
            if len(self.cache) >= self.capacity:
                # Evict the least frequently used key from the min_freq list
                evicted_key = self.freq_to_keys[self.min_freq].pop(0)
                del self.cache[evicted_key]
                del self.freq_counter[evicted_key]

            # Add new key-value pair
            self.cache[key] = value
            self.freq_counter[key] += 1
            self.min_freq = 1
            self.freq_to_keys[1].append(key)

# Example usage:
lfu_cache = LFUCache(2)
lfu_cache.put(1, 1)
lfu_cache.put(2, 2)
print(lfu_cache.get(1))  # Output: 1
lfu_cache.put(3, 3)      # Evicts key 2 as it was least frequently used
print(lfu_cache.get(2))  # Output: None (key not found)
print(lfu_cache.get(3))  # Output: 3 (newly added key)
