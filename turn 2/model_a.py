import unittest
import zlib
import io


class TestCompressionSemantics(unittest.TestCase):

    def test_compress_decompress_semantics(self):
        test_data = [
            b"Hello, World!",
            b"\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09",
            b"",
            b"\x00" * 1024,
        ]

        for data in test_data:
            compressed_data = zlib.compress(data)
            self.assertGreater(len(compressed_data), 0)
            decompressed_data = zlib.decompress(compressed_data)
            self.assertEqual(decompressed_data, data)

    def test_decompress_invalid_data(self):
        """Verify that decompression raises an error for invalid data"""
        invalid_data = [
            b"\x00" * 10,  # Truncated data
            b"\xff" * 10,  # Random garbage data
            b"\x00" * 10 + b"\x01",  # Corrupted data with extra byte
        ]

        for data in invalid_data:
            with self.assertRaises(zlib.error):
                zlib.decompress(data)

    def test_decompress_empty_data(self):
        """Verify that decompression raises an error for empty data"""
        with self.assertRaises(zlib.error):
            zlib.decompress(b"")

    def test_compress_levels(self):
        """Verify that compression levels affect data size"""
        data = b"some data to compress"
        for level in range(1, 10):
            compressed_data = zlib.compress(data, level=level)
            self.assertLessEqual(len(compressed_data), len(zlib.compress(data, level=level - 1)))


if __name__ == "__main__":
    unittest.main()
