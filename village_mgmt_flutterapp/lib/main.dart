import 'package:flutter/material.dart';

void main() => runApp(MaterialApp(title: "Village Management", home: MainActivity()));

class MainActivity extends StatefulWidget {
  @override
  _MainActivityState createState() => _MainActivityState();
}

class _MainActivityState extends State {
  String msg = 'CLICK ON BUTTON TO GET CURRENT STATUS';

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      appBar: AppBar(
        title: Text('Village Management'),
      ),
      body: Container(
        child: Center(
          child: Column(
            children: [
            SizedBox(height: 30),
              RaisedButton(
                
                child: Text("Water Status",style: TextStyle(fontSize: 30)),
                onPressed: _getWaterStatus,
                color: Colors.blue,
                textColor: Colors.white,
                padding: EdgeInsets.fromLTRB(10, 10, 10, 10),
                splashColor: Colors.grey,
              ),
              SizedBox(height: 30),
              RaisedButton(
                child: Text("Electricity Status",style: TextStyle(fontSize: 30)),
                onPressed: _getElectricityStatus,
                color: Colors.blue,
                textColor: Colors.white,
                padding: EdgeInsets.fromLTRB(10, 10, 10, 10),
                splashColor: Colors.grey,
              ),
              SizedBox(height: 30),
              RaisedButton(
                child: Text("Ration Status",style: TextStyle(fontSize: 30)),
                onPressed: _getRationStatus,
                color: Colors.blue,
                textColor: Colors.white,
                padding: EdgeInsets.fromLTRB(10, 10, 10, 10),
                splashColor: Colors.grey,
              ),
                SizedBox(height: 30),
               RaisedButton(
                child: Text("Weather Status",style: TextStyle(fontSize: 30)),
                onPressed: _getRationStatus,
                color: Colors.blue,
                textColor: Colors.white,
                padding: EdgeInsets.fromLTRB(10, 10, 10, 10),
                splashColor: Colors.grey,
              ),
              SizedBox(height: 40),
              Container ( 
                margin: const EdgeInsets.all(30.0),
                padding: const EdgeInsets.all(10.0),
                decoration: myBoxDecoration(),
                child: 
                Text(
                msg,
                style: TextStyle(fontSize: 20, fontStyle: FontStyle.italic),
                
              ))
              ,
            ],
          ),
        ),
      ),
    );
  }

  _getWaterStatus() {
    var data = "ishwar";
    setState(() {
      msg = data;
    });
  }
  _getElectricityStatus() {
    setState(() {
      if (msg.startsWith('F')) {
        msg = 'I have learned FlutterRaised example ';
      } else {
        msg = 'Flutter RaisedButton example';
      }
    });
  }
  _getRationStatus() {
    setState(() {
      if (msg.startsWith('F')) {
        msg = 'I have learned FlutterRaised example ';
      } else {
        msg = 'Flutter RaisedButton example';
      }
    });
  }
}

BoxDecoration myBoxDecoration() {
  return BoxDecoration(
    border: Border.all(),
  );
}
