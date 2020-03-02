import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:dio/dio.dart';
// import 'package:url_launcher/url_launcher.dart';
import 'dart:async';
import 'dart:convert';

void main() =>
    runApp(MaterialApp(title: "Village Management", home: MainActivity()));

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
              Row(mainAxisAlignment: MainAxisAlignment.center, children: [
                Image.asset("assets/water.png", width: 60, height: 60),
                SizedBox(width: 10),
                RaisedButton(
                  child: Text("Water Supply", style: TextStyle(fontSize: 30)),
                  onPressed: _getWaterStatus,
                  color: Colors.blue,
                  textColor: Colors.white,
                  padding: EdgeInsets.fromLTRB(10, 10, 10, 10),
                  splashColor: Colors.grey,
                ),
              ]),
              SizedBox(height: 30),
              Row(mainAxisAlignment: MainAxisAlignment.center, children: [
                Image.asset("assets/electricity.png", width: 60, height: 60),
                SizedBox(width: 10),
                RaisedButton(
                  child: Text("Electricity Supply",
                      style: TextStyle(fontSize: 30)),
                  onPressed: _getElectricityStatus,
                  color: Colors.blue,
                  textColor: Colors.white,
                  padding: EdgeInsets.fromLTRB(10, 10, 10, 10),
                  splashColor: Colors.grey,
                ),
              ]),
              SizedBox(height: 30),
              Row(mainAxisAlignment: MainAxisAlignment.center, children: [
                Image.asset("assets/ration.png", width: 60, height: 60),
                SizedBox(width: 10),
                RaisedButton(
                  child:
                      Text("Ration Delivery", style: TextStyle(fontSize: 30)),
                  onPressed: _getRationStatus,
                  color: Colors.blue,
                  textColor: Colors.white,
                  padding: EdgeInsets.fromLTRB(10, 10, 10, 10),
                  splashColor: Colors.grey,
                )
              ]),
              SizedBox(height: 30),
              Row(mainAxisAlignment: MainAxisAlignment.center, children: [
                Image.asset("assets/weather.png", width: 60, height: 60),
                SizedBox(width: 10),
                RaisedButton(
                  child: Text("Weather", style: TextStyle(fontSize: 30)),
                  onPressed: _getWeatherStatus,
                  color: Colors.blue,
                  textColor: Colors.white,
                  padding: EdgeInsets.fromLTRB(10, 10, 10, 10),
                  splashColor: Colors.grey,
                )
              ]),
              SizedBox(height: 30),
              Row(mainAxisAlignment: MainAxisAlignment.center, children: [
                Image.asset("assets/crops.png", width: 80, height: 80),
                SizedBox(width: 10),
                RaisedButton(
                  child: Text("Crops Price", style: TextStyle(fontSize: 30)),
                  onPressed: _getRationStatus,
                  color: Colors.blue,
                  textColor: Colors.white,
                  padding: EdgeInsets.fromLTRB(10, 10, 10, 10),
                  splashColor: Colors.grey,
                )
              ]),
              SizedBox(height: 40),
              Container(
                margin: const EdgeInsets.all(30.0),
                padding: const EdgeInsets.all(10.0),
                decoration: myBoxDecoration(),
                child: Column(children: [
                  Text(
                    msg,
                    style: TextStyle(fontSize: 20, fontStyle: FontStyle.italic),
                  )
                ]),
              ),
              RaisedButton(
                child: Text("HELP", style: TextStyle(fontSize: 30)),
                onPressed: _navigateHelpPage,
                color: Colors.red,
                textColor: Colors.white,
                padding: EdgeInsets.fromLTRB(10, 10, 10, 10),
                splashColor: Colors.grey,
              )
            ],
          ),
        ),
      ),
    );
  }

  _getWaterStatus() async {
    var url = 'http://192.168.0.115:5001/get_resource';
    var response = await http.get(url);
    print('Response body: ${response.body}');
    var data = json.decode(response.body);
    data = data["water"];
    setState(() {
      msg = data["resource_name"] +
          "\n" +
          "Status: " +
          data["resource_state"] +
          "\n" +
          "Time: " +
          data["resource_activation_time"] +
          "-" +
          data["resource_deactivation_time"] +
          "\n" +
          "Date: " +
          data["resource_activation_date"] +
          "-" +
          data["resource_deactivation_date"];
    });
  }

  _getElectricityStatus() async {
    var url = 'http://192.168.0.115:5001/get_resource';
    var response = await http.get(url);
    print('Response body: ${response.body}');
    var data = json.decode(response.body);
    data = data["electricity"];
    setState(() {
      msg = data["resource_name"] +
          "\n" +
          "Status: " +
          data["resource_state"] +
          "\n" +
          "Time: " +
          data["resource_activation_time"] +
          "-" +
          data["resource_deactivation_time"] +
          "\n" +
          "Date: " +
          data["resource_activation_date"] +
          "-" +
          data["resource_deactivation_date"];
    });
  }

  _getRationStatus() async {
    var url = 'http://192.168.0.115:5001/get_resource';
    var response = await http.get(url);
    print('Response body: ${response.body}');
    var data = json.decode(response.body);
    data = data["ration"];
    setState(() {
      msg = data["resource_name"] +
          "\n" +
          "Status: " +
          data["resource_state"] +
          "\n" +
          "Time: " +
          data["resource_activation_time"] +
          "-" +
          data["resource_deactivation_time"] +
          "\n" +
          "Date: " +
          data["resource_activation_date"] +
          "-" +
          data["resource_deactivation_date"];
    });
  }

  _getWeatherStatus() async {
    var url = 'http://192.168.0.115:5001/get_resource';
    var response = await http.get(url);
    print('Response body: ${response.body}');
    var data = json.decode(response.body);
    data = data["ration"];
    setState(() {
      msg = "Weather" + "\n" + "MAX TEMP: 32C" + "\n" + "PARTLY CLOUDY";
    });
  }

  _navigateHelpPage() {
    Navigator.push(
      context,
      MaterialPageRoute(builder: (context) => SecondPage()),
    );
  }
}

BoxDecoration myBoxDecoration() {
  return BoxDecoration(
    border: Border.all(),
  );
}

class SecondPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Help Page"),
      ),
      body: Container(
        child: Center(
          child: Column(
            children: [
              SizedBox(
                height: 20,
              ),
              Row(mainAxisAlignment: MainAxisAlignment.center, children: [
                Container(
                    child: RaisedButton(
                        onPressed: _noElectricityButton,
                        padding: EdgeInsets.all(0.0),
                        child: Image.asset('assets/no_electricity.jpg',
                            width: 150, height: 150))),
                SizedBox(
                  width: 20,
                ),
                Container(
                    child: RaisedButton(
                        onPressed: _noWaterButton,
                        padding: EdgeInsets.all(0.0),
                        child: Image.asset('assets/no_water.jpg',
                            width: 150, height: 150))),
              ]),
              SizedBox(
                height: 20,
              ),
              Container(
                  child: RaisedButton(
                      onPressed: _noRationButton,
                      padding: EdgeInsets.all(0.0),
                      child: Image.asset('assets/no_ration.jpg',
                          width: 150, height: 150))),
              SizedBox(
                height: 80,
              ),
              Container(
                  child: Row(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: [
                    Image.asset("assets/phone.jpg", width: 45, height: 45),
                    SizedBox(width: 15),
                    RaisedButton(
                        child: Text("Village Office",
                            style: TextStyle(fontSize: 30)),
                        onPressed: _villageOffice,
                        color: Colors.red[600],
                        textColor: Colors.white,
                        padding: EdgeInsets.fromLTRB(10, 10, 10, 10),
                        splashColor: Colors.grey),
                  ])),
              SizedBox(
                height: 20,
              ),
              Container(
                  child: Row(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: [
                    Image.asset("assets/phone.jpg", width: 45, height: 45),
                    SizedBox(width: 15),
                    RaisedButton(
                      child: Text("Central Helpline",
                          style: TextStyle(fontSize: 30)),
                      onPressed: _callCentralHepline,
                      color: Colors.red[600],
                      textColor: Colors.white,
                      padding: EdgeInsets.fromLTRB(10, 10, 10, 10),
                      splashColor: Colors.grey,
                    ),
                  ])),
            ],
          ), //column ends
        ),
      ),
    );
  }

  _noWaterButton() {
    print("NO WATER");
  }

  _noElectricityButton() {
    print("NO ELECTRICITY");
  }

  _noRationButton() {
    print("NO RATION");
  }

  _callCentralHepline() async {
    print("calling central helpline");
    // String telephoneUrl = "tel:26691781";

    // if (await canLaunch(telephoneUrl)) {
    //   await launch(telephoneUrl);
    // } else {
    //   throw "Can't phone that number.";
    // }
  }

  _villageOffice() async {
    print("calling Village Office");
    // String telephoneUrl = "tel:26691781";

    // if (await canLaunch(telephoneUrl)) {
    //   await launch(telephoneUrl);
    // } else {
    //   throw "Can't phone that number.";
    // }
  }
}
