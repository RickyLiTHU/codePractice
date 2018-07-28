class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        return False if len(moves) % 2 or moves.count('U') != moves.count('D') or moves.count('L') != moves.count('R') else True