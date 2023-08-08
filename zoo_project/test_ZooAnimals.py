import pytest
from ZooAnimals import Mouse, Whale, Catfish, Otter
from Fish import Fish
from Mammal import Mammal
from Swimmer import Swimmer
from Walker import Walker

animal_data = [
    (Mouse, "GigaHad", "Mouse", "I am a GigaHad. And I am a Mouse.", "GigaHad is walking.", Mammal, Walker),
    (Whale, "Bumba", "Whale", "I am a Bumba. And I am a Whale.", "Bumba is swimming.", Mammal, Swimmer),
    (Catfish, "Guga", "Catfish", "I am a Guga. And I am a Catfish.", "Guga is swimming.", Fish, Swimmer),
    (Otter, "Derpasonix", "Otter", "I am a Derpasonix. And I am a Otter.", "Derpasonix is walking.", Mammal, Walker),
]


@pytest.mark.parametrize("animal_class, name, species, expected_sound, expected_action, parent1, parent2",
    [
        (Mouse, "Jerry", "Mouse", "I am a Jerry. And I am a Mouse.", "Jerry is walking.", Mammal, Walker),
        (Whale, "Whaley", "Whale", "I am a Whaley. And I am a Whale.", "Whaley is swimming.", Mammal, Swimmer),
        (Catfish, "Caty", "Catfish", "I am a Caty. And I am a Catfish.", "Caty is swimming.", Fish, Swimmer),
        (Otter, "Otty", "Otter", "I am a Otty. And I am a Otter.", "Otty is walking.", Mammal, Walker),
    ]
)
def test_animals(animal_class, name, species, expected_sound, expected_action, parent1, parent2):
    animal = animal_class(name, species)

    assert animal.sound() == expected_sound

    if issubclass(animal_class, Walker):
        assert animal.walk() == expected_action
    elif issubclass(animal_class, Swimmer):
        assert animal.swim() == expected_action

    assert isinstance(animal, animal_class)
    assert isinstance(animal, parent1)
    assert isinstance(animal, parent2)


@pytest.mark.parametrize("animal_class, name, species, expected_sound, expected_action, parent1, parent2",
                         [
                             (Mouse, "", "Mouse", "I am a . And I am a Mouse.", " is walking.", Mammal, Walker),
                             (Whale, "Whaley", "", "I am a Whaley. And I am a .", "Whaley is swimming.", Mammal,
                              Swimmer),
                             (Catfish, "", "", "I am a . And I am a .", " is swimming.", Fish, Swimmer),
                             (Otter, "", "Otter", "I am a . And I am a Otter.", " is walking.", Mammal, Walker),
                         ]
                         )
def test_empty_strings(animal_class, name, species, expected_sound, expected_action, parent1, parent2):
    animal = animal_class(name, species)

    assert animal.sound() == expected_sound
    if issubclass(animal_class, Walker):
        assert animal.walk() == expected_action
    elif issubclass(animal_class, Swimmer):
        assert animal.swim() == expected_action

