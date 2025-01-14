import pytest
from RPA.core.windows.locators import MatchObject


@pytest.mark.parametrize(
    "locator, locators",
    [
        ("Robocorp", [("Name", "Robocorp", 0)]),
        ("Robocorp Window", [("Name", "Robocorp Window", 0)]),
        ("name:Robocorp Window", [("Name", "Robocorp", 0), ("Name", "Window", 0)]),
        ('name:"Robocorp Window"', [("Name", "Robocorp Window", 0)]),
        ('name:"Robocorp\'s Window"', [("Name", "Robocorp's Window", 0)]),
        (
            'name:"Robocorp\'s Window" class:"My Class"',
            [("Name", "Robocorp's Window", 0), ("ClassName", "My Class", 0)],
        ),
        (
            "Robocorp > File",
            [("Name", "Robocorp", 0), ("Name", "File", 1)],
        ),  # this isn't currently used in end-to-end logic
        (
            '"Robocorp Window93" subname:Robocorp and class:"My Class" Test regex:Robo.+',
            [
                ("Name", "Robocorp Window93", 0),
                ("SubName", "Robocorp", 0),
                ("ClassName", "My Class", 0),
                ("Name", "Test", 0),
                ("RegexName", "Robo.+", 0),
            ],
        ),
        ("Robocorp:Window", [("Name", "Robocorp:Window", 0)]),
        ("name:Robocorp:Window", [("Name", "Robocorp:Window", 0)]),
        (
            "Robocorp:Window class:Class",
            [("Name", "Robocorp:Window", 0), ("ClassName", "Class", 0)],
        ),
        (
            "Robocorp'Window Test1 class:Class classx:Classx Test2",
            [
                ("Name", "Robocorp'Window Test1", 0),
                ("ClassName", "Class", 0),
                ("Name", "classx:Classx Test2", 0),
            ],
        ),
        ("'Robocorp Window'", [("Name", "'Robocorp Window'", 0)]),
        (
            "name:'Robocorp Window'",
            [("Name", "'Robocorp", 0), ("Name", "Window'", 0)],
        ),  # single quotes don't work for enclosing, use double
        ('Robocorp" Window', [("Name", 'Robocorp" Window', 0)]),
        (
            'name:Robocorp" Window class:"My Class"',
            [("Name", 'Robocorp" Window class:', 0), ("Name", "My Class", 0)],
        ),  # enclosing quotes have to be closed properly
        (
            'name:"Robocorp" Window" class:"My Class"',
            [("Name", 'Robocorp" Window', 0), ("ClassName", "My Class", 0)],
        ),  # lucky capture
        (
            'name:"Robocorp " Window" class:"My Class"',
            [("Name", "Robocorp", 0), ("Name", 'Window" class:" My Class', 0)],
        ),  # can't capture same quote in enclosing ones
        ("", []),
        (
            "Robo and Corp or Window desktop",
            [("desktop", "desktop", 0), ("Name", "Robo Corp Window", 0)],
        ),
        (
            "id:123-456 depth:10 subname:Robo offset:100 executable:my.exe",
            [
                ("AutomationId", "123-456", 0),
                ("searchDepth", 10, 0),
                ("SubName", "Robo", 0),
                ("offset", "100", 0),
                ("executable", "my.exe", 0),
            ],
        ),
        (
            'type:Group and name:"Number pad" > type:Button and index:4',
            [
                ("ControlType", "GroupControl", 0),
                ("Name", "Number pad", 0),
                ("ControlType", "ButtonControl", 1),
                ("foundIndex", 4, 1),
            ],
        ),
    ],
)
def test_match_object(locator, locators):
    match_object = MatchObject.parse_locator(locator)
    assert match_object.locators == locators
