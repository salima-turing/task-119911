import unittest
import zlib


class TestCompressionSemantics(unittest.TestCase):

    def test_compress_decompress_semantics(self):
        # Test data with various semantic types
        test_data = [
            b"Hello, World!",  # String data
            b"\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09",  # Binary data
            b"",  # Empty data
            b"\x00" * 1024,  # Large binary data
        ]

        # Add edge cases: Invalid compressed data, corrupted data, and empty compressed data
        edge_cases = [
            b"\x00" * 10,  # Invalid compressed data (not zlib format)
            b"\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A",  # Corrupted compressed data
            b"",  # Empty compressed data
        ]

        for data in test_data:
            # Compress the data
            compressed_data = zlib.compress(data)

            # Verify that the compressed data is not empty
            self.assertGreater(len(compressed_data), 0, msg=f"Failed to compress data: {data}")

            # Decompress the data
            decompressed_data = zlib.decompress(compressed_data)

            # Verify that the decompressed data matches the original data
            self.assertEqual(decompressed_data, data, msg=f"Failed to decompress data: {data}")

        # Test for edge cases
        for edge_case in edge_cases:
            with self.assertRaises(zlib.error):
                zlib.decompress(edge_case)


if __name__ == "__main__":
    unittest.main()
