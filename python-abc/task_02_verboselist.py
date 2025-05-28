class VerboseList(list):
    """
    A custom list class that prints messages when items are added or removed.

    Inherits from the built-in list class and overrides selected methods
    (append, extend, remove, pop) to provide verbose output for each operation.
    """

    def append(self, object):
        """
        Add an item to the end of the list and print a message.

        Args:
            object: The item to add.
        """
        super().append(object)
        print(f"Added {object} to the list.")

    def extend(self, iterable):
        """
        Extend the list by appending elements from the iterable
        and print a message with the number of items added.

        Args:
            iterable (iterable): The collection of items to add.
        """
        super().extend(iterable)
        print(f"Extended the list with {len(iterable)} items.")

    def remove(self, value):
        """
        Remove the first occurrence of a value from the list
        and print a message before removing it.

        Args:
            value: The item to remove.
        """
        print(f"Removed {value} from the list.")
        super().remove(value)

    def pop(self, index=-1):
        """
        Remove and return the item at the given position (default is the last),
        and print a message with the popped item.

        Args:
            index (int, optional): The index of the item to remove. Defaults
            to -1.

        Returns:
            The item that was removed.
        """
        item = super().pop(index)
        print(f"Popped {item} from the list.")
        return item
