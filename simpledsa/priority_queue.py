from typing import Any, Callable, Optional, Union, Iterator, List, Tuple, TypeVar, Generic
import heapq

T = TypeVar('T')
P = TypeVar('P')

class PriorityQueue(Generic[T, P]):
    """
    A flexible Priority Queue implementation supporting both min-heap and max-heap behavior.
    Items can either carry their own priority or be assigned one explicitly.
    
    Args:
        key_func (Callable, optional): Function to extract priority from items.
            Default is the identity function (item is its own priority).
            For max-heap behavior, use: priority_functions.reverse
    """
    
    def __init__(self, key_func: Callable = lambda x: x):
        self._heap: List[Tuple[Any, int, T]] = []
        self._index = 0  # Used for stable sorting when priorities are equal
        self._key_func = key_func
    
    def push(self, item: T, priority: Optional[P] = None) -> None:
        """
        Add an item to the priority queue.
        
        Args:
            item: The item to be added
            priority (optional): External priority value. If not provided,
                               the item's own value will be used as priority
        """
        if priority is None:
            priority = item
        
        transformed_priority = self._key_func(priority)
        heapq.heappush(self._heap, (transformed_priority, self._index, item))
        self._index += 1
    
    def extend(self, items: Union[List[T], List[Tuple[T, P]]]) -> None:
        """
        Add multiple items to the queue.
        
        Args:
            items: Either a list of items (using self-priority) or
                  a list of (item, priority) tuples
        """
        for item in items:
            if isinstance(item, tuple) and len(item) == 2:
                self.push(item[0], item[1])
            else:
                self.push(item)
    
    def pop(self) -> T:
        """
        Remove and return the highest priority item.
        
        Returns:
            The item with the highest priority
            
        Raises:
            IndexError: If the queue is empty
        """
        if self.is_empty():
            raise IndexError("pop from an empty priority queue")
        return heapq.heappop(self._heap)[2]
    
    def peek(self) -> T:
        """
        Return the highest priority item without removing it.
        
        Returns:
            The item with the highest priority
            
        Raises:
            IndexError: If the queue is empty
        """
        if self.is_empty():
            raise IndexError("peek at an empty priority queue")
        return self._heap[0][2]
    
    def is_empty(self) -> bool:
        """Check if the priority queue is empty."""
        return len(self._heap) == 0
    
    def __len__(self) -> int:
        """Return the number of items in the queue."""
        return len(self._heap)
    
    def __bool__(self) -> bool:
        """Return True if the queue is not empty."""
        return bool(self._heap)
    
    def __iter__(self) -> Iterator[T]:
        """
        Iterate through items in priority order without removing them.
        
        Returns:
            Iterator yielding items in priority order
        """
        return iter(item for _, _, item in sorted(self._heap))
    
    def pop_all(self) -> Iterator[T]:
        """
        Iterate through and remove all items in priority order.
        
        Returns:
            Iterator yielding items in priority order
        """
        while self:
            yield self.pop()
    
    def __enter__(self) -> 'PriorityQueue[T, P]':
        """Enter the context manager."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """Exit the context manager, clearing the queue."""
        self._heap.clear()
        self._index = 0
    
    @classmethod
    def from_items(cls, items: List[T], key_func: Callable = lambda x: x) -> 'PriorityQueue[T, P]':
        """
        Create a PriorityQueue from a list of items.
        
        Args:
            items: List of items to add to the queue
            key_func: Optional priority function
            
        Returns:
            New PriorityQueue containing the items
        """
        pq = cls(key_func)
        pq.extend(items)
        return pq
    
    @classmethod
    def from_pairs(cls, pairs: List[Tuple[T, P]], key_func: Callable = lambda x: x) -> 'PriorityQueue[T, P]':
        """
        Create a PriorityQueue from a list of (item, priority) pairs.
        
        Args:
            pairs: List of (item, priority) tuples
            key_func: Optional priority function
            
        Returns:
            New PriorityQueue containing the items
        """
        pq = cls(key_func)
        pq.extend(pairs)
        return pq
    
    @classmethod
    def merge(cls, queues: List['PriorityQueue[T, P]']) -> 'PriorityQueue[T, P]':
        """
        Merge multiple PriorityQueues into a new one.
        
        Args:
            queues: List of PriorityQueues to merge
            
        Returns:
            New PriorityQueue containing all items
        
        Note:
            All queues must use the same key_func
        """
        if not queues:
            return cls()
        
        # Use the key_func from the first queue
        merged = cls(queues[0]._key_func)
        for queue in queues:
            if queue._key_func != merged._key_func:
                raise ValueError("All queues must use the same key_func")
            merged._heap.extend(queue._heap)
        
        # Reheapify the merged heap
        heapq.heapify(merged._heap)
        return merged