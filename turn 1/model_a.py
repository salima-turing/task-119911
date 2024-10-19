import unittest


def rle_encode(data):
    encoded = []
    if not data:
        return encoded

    char = data[0]
    count = 1
    for i in range(1, len(data)):
        if data[i] == char:
            count += 1
        else:
            encoded.append((char, count))
            char = data[i]
            count = 1
    encoded.append((char, count))
    return encoded


def rle_decode(encoded_data):
    decoded = []
    for char, count in encoded_data:
        decoded.extend([char] * count)
    return "".join(decoded)


class TestRLE(unittest.TestCase):

    def test_rle_semantic_integrity(self):
        test_data = [
            ("", []),
            ("a", [("a", 1)]),
            ("aaabbcc", [("a", 3), ("b", 2), ("c", 2)]),
            ("abacabad", [("a", 1), ("b", 1), ("a", 1), ("c", 1), ("a", 1), ("b", 1), ("d", 1)]),
            ("hello", [("h", 1), ("e", 1), ("l", 2), ("o", 1)]),
        ]

        for original_data, expected_encoding in test_data:
            with self.subTest(data=original_data):
                # Verify encoding
                encoded = rle_encode(original_data)
                self.assertEqual(encoded, expected_encoding,
                                 f"RLE encoding failed for '{original_data}': Expected {expected_encoding}, got {encoded}")

                # Verify decoding
                decoded = rle_decode(encoded)
                self.assertEqual(decoded, original_data,
                                 f"RLE decoding failed for '{encoded}': Expected {original_data}, got {decoded}")


if __name__ == '__main__':
    unittest.main()
