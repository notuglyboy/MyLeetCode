    def firstBadVersion(self, n):
        start = 0
        end = n
        while start < end:
            mid = int((start + end) / 2)
            if isBadVersion(mid):
                end = mid
            else:
                start = mid + 1

        return start