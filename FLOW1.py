[
    {
        "id": "20688228.6b3c3e",
        "type": "tab",
        "label": "1-Flow 3",
        "disabled": false,
        "info": ""
    },
    {
        "id": "de01ed27.5587f",
        "type": "rpi-gpio in",
        "z": "20688228.6b3c3e",
        "name": "Button",
        "pin": "7",
        "intype": "up",
        "debounce": "25",
        "read": false,
        "x": 110,
        "y": 60,
        "wires": [
            [
                "75e379ee.251be8",
                "e33ed2e4.3528d"
            ]
        ]
    },
    {
        "id": "84c4b3ed.b415b",
        "type": "rpi-gpio out",
        "z": "20688228.6b3c3e",
        "name": "LED",
        "pin": "11",
        "set": true,
        "level": "0",
        "freq": "",
        "out": "out",
        "x": 630,
        "y": 160,
        "wires": []
    },
    {
        "id": "75e379ee.251be8",
        "type": "debug",
        "z": "20688228.6b3c3e",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "false",
        "x": 540,
        "y": 60,
        "wires": []
    },
    {
        "id": "e33ed2e4.3528d",
        "type": "switch",
        "z": "20688228.6b3c3e",
        "name": "if input is 1",
        "property": "payload",
        "propertyType": "msg",
        "rules": [
            {
                "t": "eq",
                "v": "1",
                "vt": "str"
            },
            {
                "t": "else"
            }
        ],
        "checkall": "true",
        "repair": false,
        "outputs": 2,
        "x": 250,
        "y": 140,
        "wires": [
            [
                "54b5faf1.b4be44"
            ],
            [
                "e673f0dd.39899"
            ]
        ]
    },
    {
        "id": "54b5faf1.b4be44",
        "type": "change",
        "z": "20688228.6b3c3e",
        "name": "Change to 0",
        "rules": [
            {
                "t": "set",
                "p": "payload",
                "pt": "msg",
                "to": "0",
                "tot": "str"
            }
        ],
        "action": "",
        "property": "",
        "from": "",
        "to": "",
        "reg": false,
        "x": 440,
        "y": 140,
        "wires": [
            [
                "84c4b3ed.b415b"
            ]
        ]
    },
    {
        "id": "e673f0dd.39899",
        "type": "change",
        "z": "20688228.6b3c3e",
        "name": "Change to 1",
        "rules": [
            {
                "t": "set",
                "p": "payload",
                "pt": "msg",
                "to": "1",
                "tot": "str"
            }
        ],
        "action": "",
        "property": "",
        "from": "",
        "to": "",
        "reg": false,
        "x": 420,
        "y": 240,
        "wires": [
            [
                "84c4b3ed.b415b"
            ]
        ]
    }
]
