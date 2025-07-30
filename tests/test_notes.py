import unittest
from notes import frequencies, C_freq, CSharp_freq, D_freq, DSharp_freq, E_freq, F_freq, FSharp_freq, G_freq, GSharp_freq, A_freq, ASharp_freq, B_freq

class TestNotes(unittest.TestCase):

    def test_frequencies_not_empty(self):
        self.assertTrue(frequencies)

    def test_specific_note_frequency(self):
        self.assertEqual(frequencies['A4'], 440.00)

    def test_c_freq_list(self):
        self.assertIn(16.35, C_freq)
        self.assertIn(4186.01, C_freq)
        self.assertEqual(len(C_freq), 9)

    def test_csharp_freq_list(self):
        self.assertIn(17.32, CSharp_freq)
        self.assertEqual(len(CSharp_freq), 9)

    def test_d_freq_list(self):
        self.assertIn(18.35, D_freq)
        self.assertEqual(len(D_freq), 9)

    def test_dsharp_freq_list(self):
        self.assertIn(19.45, DSharp_freq)
        self.assertEqual(len(DSharp_freq), 9)

    def test_e_freq_list(self):
        self.assertIn(20.60, E_freq)
        self.assertEqual(len(E_freq), 9)

    def test_f_freq_list(self):
        self.assertIn(21.83, F_freq)
        self.assertEqual(len(F_freq), 9)

    def test_fsharp_freq_list(self):
        self.assertIn(23.12, FSharp_freq)
        self.assertEqual(len(FSharp_freq), 9)

    def test_g_freq_list(self):
        self.assertIn(24.50, G_freq)
        self.assertEqual(len(G_freq), 9)

    def test_gsharp_freq_list(self):
        self.assertIn(25.96, GSharp_freq)
        self.assertEqual(len(GSharp_freq), 9)

    def test_a_freq_list(self):
        self.assertIn(27.50, A_freq)
        self.assertEqual(len(A_freq), 9)

    def test_asharp_freq_list(self):
        self.assertIn(29.14, ASharp_freq)
        self.assertEqual(len(ASharp_freq), 9)

    def test_b_freq_list(self):
        self.assertIn(30.87, B_freq)
        self.assertEqual(len(B_freq), 9)

if __name__ == '__main__':
    unittest.main()
