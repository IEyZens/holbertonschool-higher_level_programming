class CountedIterator:
    """
    An iterator wrapper that counts how many items have been iterated over.

    This class wraps around any iterable object and provides an iterator
    interface. It overrides the __next__ method to count the number of items
    returned so far, accessible via the get_count() method.
    """

    def __init__(self, obj):
        """
        Initialize the CountedIterator with the given iterable.

        Args:
            obj (iterable): The iterable to wrap and iterate over.
        """
        self.__iterator = iter(obj)
        self.__count = 0

    def __next__(self):
        """
        Return the next item from the iterator and increment the count.

        Returns:
            object: The next item in the iteration.

        Raises:
            StopIteration: If there are no more items.
        """
        item = next(self.__iterator)
        self.__count += 1
        return item

    def get_count(self):
        """
        Return the number of items that have been iterated over so far.

        Returns:
            int: The number of times __next__ has been successfully called.
        """
        return self.__count
