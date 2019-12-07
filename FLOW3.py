[
    {
        "id": "64754915.ecec28",
        "type": "tab",
        "label": "1-Flow 5",
        "disabled": false,
        "info": ""
    },
    {
        "id": "1444bd4f.2657b3",
        "type": "inject",
        "z": "64754915.ecec28",
        "name": "",
        "topic": "",
        "payload": "",
        "payloadType": "date",
        "repeat": "5",
        "crontab": "",
        "once": true,
        "onceDelay": 0.1,
        "x": 140,
        "y": 220,
        "wires": [
            [
                "f1927cd0.068e4"
            ]
        ]
    },
    {
        "id": "f1927cd0.068e4",
        "type": "function",
        "z": "64754915.ecec28",
        "name": "Payload",
        "func": "msg.headers={\n    deviceKey: \"3Ut1MudzASdC4L7L\"\n}\nmsg.payload= \"Temperature,,25.3\";\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 380,
        "y": 300,
        "wires": [
            [
                "838c24a3.97e638"
            ]
        ]
    },
    {
        "id": "838c24a3.97e638",
        "type": "http request",
        "z": "64754915.ecec28",
        "name": "",
        "method": "POST",
        "ret": "txt",
        "paytoqs": false,
        "url": "https://api.mediatek.com/mcs/v2/devices/DB0kLp45/datapoints.csv",
        "tls": "",
        "persist": false,
        "proxy": "",
        "authType": "",
        "x": 560,
        "y": 300,
        "wires": [
            [
                "8fe7b873.8dede8",
                "5483afe.c81515"
            ]
        ]
    },
    {
        "id": "8fe7b873.8dede8",
        "type": "debug",
        "z": "64754915.ecec28",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "false",
        "x": 760,
        "y": 400,
        "wires": []
    },
    {
        "id": "5483afe.c81515",
        "type": "http response",
        "z": "64754915.ecec28",
        "name": "",
        "statusCode": "",
        "headers": {},
        "x": 750,
        "y": 300,
        "wires": []
    }
]
