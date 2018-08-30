class Solution(object):
    def parse_pattern(self, p):
        pattern_stack = []
        l_s = 0
        for i in p:
            if i == '*':
                if l_s > 0:
                    l = pattern_stack.pop()
                    l2 = (l[0], '*')
                    pattern_stack.append(l2)
                else:
                    return {}, set()
            else:
                pattern_stack.append((i, 1))
                l_s += 1
        state_transitions = {-1: {}}

        last_states = {-1}
        for ind, i in enumerate(pattern_stack):
            cur_states = set()
            for j in last_states:
                if j not in state_transitions:
                    state_transitions[j] = {}

                if i[0] not in state_transitions[j]:
                    state_transitions[j][i[0]] = set()
                state_transitions[j][i[0]].add(ind)
                cur_states.add(ind)
                if i[1] == '*':
                    if ind not in state_transitions:
                        state_transitions[ind] = {}
                    if i[0] not in state_transitions[ind]:
                        state_transitions[ind][i[0]] = set()
                    state_transitions[ind][i[0]].add(ind)
                    cur_states.add(j)
            last_states = cur_states

        accept_states = set()

        for i in range(l_s - 1, -2, -1):
            accept_states.add(i)
            if i < 0 or pattern_stack[i][1] != '*':
                break
        return state_transitions, accept_states

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        state_transitions, accept_states = self.parse_pattern(p)
        states = {-1}

        for i in s:
            cur_states = set()
            for st in states:
                if st in state_transitions:
                    if i in state_transitions[st]:
                        cur_states.update(state_transitions[st][i])
                    if '.' in state_transitions[st]:
                        cur_states.update(state_transitions[st]['.'])

            if len(cur_states) == 0:
                return False

            states = cur_states

        for s in states:
            if s in accept_states:
                return True
        return False