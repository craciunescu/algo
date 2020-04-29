# Mergesort.

def merge_sort(values):

    def merge(data, low, mid, high):
        ordered = []
        left = low
        right = mid+1

        # While in range.
        while left <= mid and right <= high:
            if data[left] <= data[right]:
                ordered.append(data[left])
                left += 1
            else:
                ordered.append(data[right])
                right += 1

        # Unbalanced halves.
        while left <= mid:
            ordered.append(data[left])
            left += 1
        while right <= high:
            ordered.append(data[right])
            right += 1

        for idx, val in enumerate(ordered):
            data[low + idx] = val

    def sort(data, low, high):
        if low < high:
            mid = (low + high) // 2

            sort(data, low, mid)
            sort(data, mid+1, high)
            merge(data, low, mid, high)

    sort(values, 0, len(values)-1)
    return values
