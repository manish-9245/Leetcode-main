class Solution:
	def minSpeedOnTime(self, dist: List[int], hour: float) -> int:

		result = -1

		left , right = 1 , 10**9

		while left <= right:

			mid = (left + right) // 2

			total_time = 0

			for index in range(len(dist)):

				if index != (len(dist) - 1):
					total_time = total_time + math.ceil(dist[index] / mid )

				else:
					total_time = total_time + dist[index] / mid

			if total_time <= hour:
				result = mid

				right = mid - 1

			elif total_time > hour:
				left = mid + 1

		return result