class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_count = Counter(words)
        heap = []
        for word, count in word_count.items():
            heapq.heappush(heap, (-count, word))
        top_k = []
        for _ in range(k):
            top_k.append(heapq.heappop(heap)[1])
        return top_k