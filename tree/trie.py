class TrieNode:
  def __init__(self, char = ''):
    self.children = [None] * 26
    self.char = char
    self.is_word = False

  def mark_word(self):
    self.is_word = True


class Trie:
  def __init__(self):
    self.root = TrieNode()

  def get_index(self, t):
    return ord(t) - ord('a')

  def insert(self, key):
    if key is None:
      return

    current_node = self.root

    for i in range(len(key)):
      current_index = self.get_index(key[i])

      if current_node.children[current_index] is None:
        current_node.children[current_index] = TrieNode(key[i])

      current_node = current_node.children[current_index]

    current_node.mark_word()

  def search(self, key):
    if key is None:
      return False

    current_node = self.root

    for i in range(len(key)):
      current_index = self.get_index(key[i])

      if current_node.children[current_index] is None:
        return False

      current_node = current_node.children[current_index]

    if current_node is not None and current_node.is_word:
      return True

    return False

# Input keys (use only 'a' through 'z')
keys = ["the", "a", "there", "answer", "any",
        "by", "bye", "their", "abc"]
output = ["Not present in trie", "Present in trie"]

t = Trie()
print("Keys to insert: ")
print(keys)

# Construct Trie
for i in range(len(keys)):
    t.insert(keys[i])

# Search for different keys
if t.search("the") is True:
    print("the --- " + output[1])
else:
    print("the --- " + output[0])

if t.search("these") is True:
    print("these --- " + output[1])
else:
    print("these --- " + output[0])

if t.search("abc") is True:
    print("abc --- " + output[1])
else:
    print("abc --- " + output[0])