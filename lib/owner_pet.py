class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []
    def __init__(self,name,pet_type,owner = None):
        self.name = name
        self.pet_type = pet_type
        self._owner = owner
        Pet.all.append(self)
    @property
    def pet_type(self):
        return self._pet_type
    @pet_type.setter
    def pet_type(self,pet_type):
        if isinstance(pet_type,str) and pet_type in Pet.PET_TYPES:
            self._pet_type = pet_type
        else: 
            raise Exception('the pet_type must be a string and must be in the PET_Types list')
    @property
    def owner(self):
        return self._owner
    @owner.setter
    def owner(self,owner):
        if isinstance(owner,Owner):
            self._owner = owner
        


class Owner:
    all_pets = []
    def __init__(self,name):
        self.name = name
        self.owner_pets = []
        
   
    def pets(self):
        all_pets = Pet.all
        for pet in all_pets:
            
            print(pet._owner)
            if pet._owner == self:
                self.owner_pets.append(pet)
        
        print(self.owner_pets)
        return self.owner_pets
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception('pet mus be an instance of Pet')
        pet._owner = self
        
    def get_sorted_pets(self):
        pets = []
        for pet in Pet.all:
            if pet._owner == self:
                pets.append(pet)
        sorted_pets = sorted(pets, key = lambda pet: pet.name)
        return sorted_pets
owner = Owner("Ben")
pet1 = Pet("Fido", "dog", owner)
pet2 = Pet("Clifford", "dog", owner)
# print(pet1)
owner.pets()
