class Solution:
    def makeBalanced(self, input):

        current_index = 0
        byte_array_input = bytearray(input)
        valid_counter = 0

        # Forward pass
        while current_index < len(byte_array_input):
            if chr(byte_array_input[current_index]) == '(':
                valid_counter += 1
            elif chr(byte_array_input[current_index]) == ')':
                valid_counter -= 1

            if valid_counter < 0:
                del byte_array_input[current_index]
                valid_counter += 1
                current_index -= 1

            current_index += 1

        if valid_counter > 0:
            # Backward pass
            valid_counter = 0
            current_index = len(byte_array_input) - 1
            while current_index >= 0:
                if chr(byte_array_input[current_index]) == ')':
                    valid_counter += 1
                elif chr(byte_array_input[current_index]) == '(':
                    valid_counter -= 1

                if valid_counter < 0:
                    del byte_array_input[current_index]
                    valid_counter += 1

                current_index -= 1

        return str(byte_array_input)

solution = Solution()

print(solution.makeBalanced('((()))))()())())(()'))
