from outils import plus_grands_influenceurs

class TestPlusGrandsInfluenceurs():
    def test_cas_simple(self):
        reseau = {
            'Sellia': ['Léa', 'Heidi'],
            'Léa': ['Heidi'],
            'Heidi': ['Léa']
        }
        self.assertEqual(plus_grands_influenceurs(reseau), ['Léa', 'Heidi'])
    
    def test_reseau_vide(self):
        reseau = {}
        self.assertEqual(plus_grands_influenceurs(reseau), [])
    
    def test_unique_influenceur(self):
        reseau = {
            'Sellia': ['Heidi'],
            'Léa': ['Heidi'],
            'Heidi': []
        }
        self.assertEqual(plus_grands_influenceurs(reseau), ['Heidi'])
    
    def test_personne_isolee(self):
        reseau = {
            'Sellia': [],
            'Léa': [],
            'Heidi': []
        }
        self.assertEqual(set(plus_grands_influenceurs(reseau)), {'Sellia', 'Léa', 'Heidi'})

if __name__ == '__main__':
    TestPlusGrandsInfluenceurs()