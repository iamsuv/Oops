

class Country:
    def __init__(self,name,population,area):
        self.name=name
        self.population=population
        self.area=area
    def __repr__(self):
        return (self.name,self.population,self.area)


countries=[Country('India','120','100'),Country('China','150','200'),Country('US','80','150')]
countries.append([Country('UK','75','80')])
print(countries)