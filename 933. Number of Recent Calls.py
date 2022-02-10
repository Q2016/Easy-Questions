Question:
You have a RecentCounter class which counts the number of recent requests within a certain time frame.
Implement the RecentCounter class:
RecentCounter() Initializes the counter with zero recent requests.
int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, and returns the number of requests that has 
happened in the past 3000 milliseconds (including the new request). Specifically, return the number of requests that have happened in the 
inclusive range [t - 3000, t]. It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.

Example 1:
Input
["RecentCounter", "ping", "ping", "ping", "ping"]
[[], [1], [100], [3001], [3002]]
Output
[null, 1, 2, 3, 3]
Explanation
RecentCounter recentCounter = new RecentCounter();
recentCounter.ping(1);     // requests = [1], range is [-2999,1], return 1
recentCounter.ping(100);   // requests = [1, 100], range is [-2900,100], return 2
recentCounter.ping(3001);  // requests = [1, 100, 3001], range is [1,3001], return 3
recentCounter.ping(3002);  // requests = [1, 100, 3001, 3002], range is [2,3002], return 3


Solution: Sliding Window

Now that we've clarified the nature of the problem, it shall not be difficult to come up with a solution. In fact, the solution is as simple as 
iterating through an array or a list. The idea is that we can use a container such as array or list to keep track of all the 
incoming ping calls. At each occasion of ping(t) call, first we append the call to the container, and then starting from the current call, 
we iterate backwards to count the calls that fall into the time range of [t-3000, t].
Before rushing to the implementation, let us dwell on the problem a bit more, since there are still plenty of things we could optimize.
One observation is that the sequence is ever-growing, so as our container. On the other hand, once the ping calls become outdated, i.e. out 
of the scope of [t-3000, t], we do not need to keep them any longer in the container, since they will not contribute to the solution later.
As a result, one optimization that we could do is that rather than keeping all the historical ping calls in the container, we could remove the 
outdated calls on the go, which can avoid the overflow of the container and reduce the memory consumption to the least.
In summary, our container will function like a sliding window over the ever-growing sequence of ping calls.

sliding window
Based on the above description, the list data structure seems to be more fit as the container for our tasks, than the array. Because the 
list is more adapted for the following two operations:
Appending: we will append each incoming call to the tail of the sliding window.
Popping: we need to pop out all the outdated calls from the head of the sliding window.

class RecentCounter:

    def __init__(self):
        self.slide_window = deque()

    def ping(self, t: int) -> int:
        # step 1). append the current call
        self.slide_window.append(t)

        # step 2). invalidate the outdated pings
        while self.slide_window[0] < t - 3000:
            self.slide_window.popleft()

        return len(self.slide_window)
