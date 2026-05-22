/*
---------------------------------------------------------------------------------------
Developer: Ferhat Gönültaş
Contact: alonewolfsupp@gmail.com
GitHub: https://github.com/ferhatgnlts
--------------------------------------------------------------------------------------
Licenses:
This project was developed using the Three.js library,
which is released under the MIT License.
(URL): https://github.com/mrdoob/three.js/
---------------------------------------------------------------------------------------
*/

app.SetScreenMode( "Full" )
app.SetOrientation( "Landscape" )
//Called when application is started.
function OnStart()
{
	//Create a layout with objects vertically centered.
	lay = app.CreateLayout( "Linear", "VCenter,FillXY" )

	//Create a text label and add it to layout.
	webview = app.CreateWebView( 1,1, "IgnoreErrors" )
	webview.LoadUrl( "index.html" )
	webview.SetOnConsole( function ( con, a, b) { alert(con+a+b) } )
	lay.AddChild( webview )
	
	//Add layout to app.	
	app.AddLayout( lay )
}
