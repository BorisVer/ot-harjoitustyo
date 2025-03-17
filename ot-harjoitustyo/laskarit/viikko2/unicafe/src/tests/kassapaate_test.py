import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_kassapaate_oikea_alkusumma(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_lounaita_myyty_alussa_nolla(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kateisosto_rahasumma_nousee_edullinen(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_kateisosto_rahasumma_nousee_maukkaan(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_kateisosto_myytyjen_maara_nousee_edullinen(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kateisosto_myytyjen_maara_nousee_maukkaan(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kateisosto_liian_vahan_rahaa_ei_nosta_kassaa_edullinen(self):
        self.kassapaate.syo_edullisesti_kateisella(239)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kateisosto_liian_vahan_rahaa_ei_nosta_kassaa_maukkaan(self):
        self.kassapaate.syo_maukkaasti_kateisella(399)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kateisosto_liian_vahan_rahaa_ei_nosta_myytyjen_maara_edullinen(self):
        self.kassapaate.syo_edullisesti_kateisella(239)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kateisosto_liian_vahan_rahaa_ei_nosta_myytyjen_maara_maukkaan(self):
        self.kassapaate.syo_maukkaasti_kateisella(399)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kortilta_veloitetaan_tarpeeksi_edullinen(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo , 760)

    def test_kortilta_veloitetaan_tarpeeksi_maukkaan(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo , 600)

    def test_kortti_ostos_menee_lapi_jos_tarpeeksi_edullinen(self):
        self.assertTrue(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti))

    def test_kortti_ostos_menee_lapi_jos_tarpeeksi_maukkaan(self):
        self.assertTrue(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti))

    def test_kortti_ostos_nostaa_myytyjen_maaraa_edullinen(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kortti_ostos_nostaa_myytyjen_maaraa_maukkaan(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kortin_saldo_ei_riita_kortin_saldo_ei_muutu_edullinen(self):
        kortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(kortti.saldo , 100)

    def test_kortin_saldo_ei_riita_kortin_saldo_ei_muutu_maukkaan(self):
        kortti = Maksukortti(100)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(kortti.saldo , 100)

    def test_kortin_saldo_ei_riita_ei_muuta_myytyjen_maara_edullinen(self):
        kortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kortin_saldo_ei_riita_ei_muuta_myytyjen_maara_maukkaan(self):
        kortti = Maksukortti(100)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kortin_saldo_ei_riita_myynti_ei_onnistu_edullinen(self):
        kortti = Maksukortti(100)
        self.assertFalse(self.kassapaate.syo_edullisesti_kortilla(kortti))

    def test_kortin_saldo_ei_riita_myynti_ei_onnistu_maukkaan(self):
        kortti = Maksukortti(100)
        self.assertFalse(self.kassapaate.syo_maukkaasti_kortilla(kortti))

    def test_kassan_rahaa_ei_muutu_kortilla_edullinen(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kassan_rahaa_ei_muutu_kortilla_maukkaan(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortin_saldo_muuttuu_kun_ladataan(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)
        self.assertEqual(self.maksukortti.saldo, 1100)

    def test_negaviivisen_summan_lataaminen_kortille(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100)
        self.assertEqual(self.maksukortti.saldo, 1000)

    def test_euroina_sama_kuin_sentteina(self):
        rahaa = self.kassapaate.kassassa_rahaa_euroina()
        self.assertEqual(rahaa, 1000.00)
