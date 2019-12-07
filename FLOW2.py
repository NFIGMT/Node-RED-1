[
    {
        "id": "a95cf688.960538",
        "type": "tab",
        "label": "1-Flow 4",
        "disabled": false,
        "info": ""
    },
    {
        "id": "e2d89c9.a67fa6",
        "type": "inject",
        "z": "a95cf688.960538",
        "name": "",
        "topic": "",
        "payload": "",
        "payloadType": "date",
        "repeat": "5",
        "crontab": "",
        "once": true,
        "onceDelay": 0.1,
        "x": 280,
        "y": 280,
        "wires": [
            [
                "653844e1.24c8dc"
            ]
        ]
    },
    {
        "id": "653844e1.24c8dc",
        "type": "function",
        "z": "a95cf688.960538",
        "name": "Payload",
        "func": "msg.headers={\n    devicekey: \"006sxTxBL8BF300Z\"\n};\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 440,
        "y": 340,
        "wires": [
            [
                "b6957690.29fef8"
            ]
        ]
    },
    {
        "id": "b6957690.29fef8",
        "type": "http request",
        "z": "a95cf688.960538",
        "name": "",
        "method": "GET",
        "ret": "txt",
        "paytoqs": false,
        "url": "http://api.mediatek.com/mcs/v2/devices/D4UhSkiQ/datachannels/LEDControl/datapoints.csv",
        "tls": "",
        "persist": false,
        "proxy": "",
        "authType": "",
        "x": 600,
        "y": 340,
        "wires": [
            [
                "5d541507.b9d9fc",
                "d2f95b4a.e695f8"
            ]
        ]
    },
    {
        "id": "5d541507.b9d9fc",
        "type": "http response",
        "z": "a95cf688.960538",
        "name": "",
        "statusCode": "",
        "headers": {},
        "x": 800,
        "y": 340,
        "wires": []
    },
    {
        "id": "d2f95b4a.e695f8",
        "type": "debug",
        "z": "a95cf688.960538",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "payload",
        "targetType": "msg",
        "x": 840,
        "y": 460,
        "wires": []
    }
]
