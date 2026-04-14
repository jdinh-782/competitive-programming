# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
import base64

class Solution:
    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return base64.b64encode(' '.encode("utf-8")).decode("utf-8")

        # Join `strs` together to create a new string type
        s = " ".join(strs)

        # Return the encoded version as a string
        return base64.b64encode(s.encode("utf-8")).decode("utf-8")

    def decode(self, s: str) -> List[str]:
        if s == ' ':
            return []

        # Decode the encoded strings and split by delimiter into list of strings
        decoded_bytes = base64.b64decode(s)
        decoded_str = decoded_bytes.decode('utf-8')

        # Complexity Analysis
        # Time Complexity O(N): Joining the strings initally, converting them to bytes through encode(), and applying base64
        #                       requires iterating over the data, which scales linearly with total length of the text
        # Space Complexity O(N): Allocating new memory for the joined strings, the encoded byte arrays, and the final decoded list
        #                        scales linearly with the input size
        return decoded_str.split(' ')

    
    def encodeOptimized(self, strs: List[str]) -> str:
        # Manually build the encoded string by prefixing each str element with its exact length and delimiter '#'
        encoded_string = ""
        for s in strs:
            # Format: <length>#<string>
            encoded_string += str(len(s)) + "#" + s
        return encoded_string

    def decodeOptimized(self, s: str) -> List[str]:
        # Iterate through "encoded" string using a while loop with pointers
        decoded_list = []
        i = 0
        
        while i < len(s):
            j = i

            # Look forward to find the delimiter '#'
            while s[j] != "#":
                j += 1
            
            # The length of the string is everything between i and j
            length = int(s[i:j])
            
            # The actual string starts right after '#' and spans 'length' characters
            start = j + 1
            end = start + length
            decoded_list.append(s[start:end])
            
            # Move the pointer to the start of the next length-prefix
            i = end
    
        # Complexity Analysis
        # Time Complexity O(N): Both encode and decode functions execute in linear time. During encoding, calculating lengths and
        #                       concatenating strings requires visiting each character. During decoding, pointers `i` and `j` move
        #                       strictly forward through the string, meaning every character is evaluated exactly once
        # Space Complexity O(N): For both functions, we need to allocate memory for the output. Encoding creates a new string of size N
        #                        Decoding creates an array containing N characters
        return decoded_list