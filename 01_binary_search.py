class BinarySearch():

    def search_iterative(self, arr: list[int], item):
        # low and high keep track of which part of the list you'll search in.
        low = 0
        high = len(arr) - 1
        # While you haven't narrowed it down to one element ...
        while low <= high:
            # ... check the middle element
            mid = (low + high) // 2
            guess = arr[mid]
            # Found the item.
            if guess == item:
                return f"index is: {mid}, num is: {arr[mid]}"
            # The guess was too high.
            if guess > item:
                high = mid - 1
            # The guess was too low.
            else:
                low = mid + 1

        # Item doesn't exist
        return None


if __name__ == "__main__":
    # We must initialize the class to use the methods of this class
    bs = BinarySearch()
    my_list = [1, 3, 5, 7, 9]

    print(bs.search_iterative(my_list, 3))  # => 1 -это индекса числа которого мы ищем(3)
