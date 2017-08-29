<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <meta name="fragment" content="!">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="Keywords" content="GeoForm, GeoForm Template, Template, Map, Esri">
    <meta name="description" content="GeoForm is a configurable template for form based data editing of a Feature Service. This application allows users to enter data through a form instead of a map’s pop-up while leveraging the power of the Web Map and editable Feature Services.">
    <meta name="author" content="esri">
    <!-- Facebook -->
    <meta property="og:title" content="GeoForm">
    <meta property="og:image" content="images/item.png">
    <meta property="og:site_name" content="esri">
    <!-- Chrome for Android -->
    <link rel="apple-touch-icon" href="images/apple-touch-icon.png">
    <title>GeoForm</title>
    <!-- Bootstrap core CSS -->
    <!-- Latest compiled and minified CSS -->
    <link rel="stylesheet" type="text/css" href="js/vendor/bootstrap/css/bootstrap.min.css">
    <link rel="stylesheet" type="text/css" href="js/vendor/bootstrap-datetimepicker/css/bootstrap-datetimepicker.min.css">
    <link rel="stylesheet" type="text/css" href="https://js.arcgis.com/3.21/esri/css/esri.css">
    <link rel="stylesheet" type="text/css" href="https://js.arcgis.com/3.21/dijit/themes/claro/claro.css">
    <link rel="stylesheet" type="text/css" href="js/vendor/font-awesome/css/font-awesome.min.css">
    <link rel="stylesheet" type="text/css" href="css/style.css">
    <link id="rtlCSS" rel="stylesheet" />
    <link href="js/vendor/select2/select2.min.css" rel="stylesheet" />
    <link href="js/vendor/touch-spinner/jquery.bootstrap-touchspin.min.css" rel="stylesheet" type="text/css" />
    <script src="js/vendor/jquery.min.js"></script>
    <script src="js/vendor/moment-with-langs.min.js"></script>
    <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
    <script src="js/vendor/html5shiv.min.js"></script>
    <script src="js/vendor/respond.min.js"></script>
    <![endif]-->
</head>

<body id="geoform" class="claro app-loading">
    <a id="top"><!-- Top of page --></a>
    <div class="loading-indicator">
        <div class="icon-loading"></div>
        <div class="loading-error">
            <div class="alert alert-danger"><span class="icon-frown"></span> <span id="loading_message"></span>
            </div>
        </div>
    </div>
    <div id="fullscreen_container" class="fullscreen-container"></div>
    <div id="parentContainter" class="app-content"></div>
    <script type="text/javascript">
        var package_path = window.location.pathname.substring(0, window.location.pathname.lastIndexOf('/'));
        var dojoConfig = {
            // The locationPath logic below may look confusing but all its doing is
            // enabling us to load the api from a CDN and load local modules from the correct location.
            packages: [{
                name: "application",
                location: package_path + '/js'
            }, {
                name: "config",
                location: package_path + '/config'
            }, {
                name: "arcgis_templates",
                location: package_path + '/..'
            }, {
                name: "vendor",
                location: package_path + '/js/vendor'
            }, {
                name: "views",
                location: package_path + '/views'
            }]
        };
        // Have to handle a locale parameter before dojo is loaded
        if (location.search.match(/locale=([\w-]+)/)) {
          dojoConfig.locale = RegExp.$1;
        }
    </script>
    <script type="text/javascript" src="https://js.arcgis.com/3.21"></script>
    <script type="text/javascript" src="js/vendor/offline/offline.min.js"></script>
    <script type="text/javascript" src="js/vendor/IndexedDBShim.min.js"></script>
    <script type="text/javascript">
        require(["config/templateConfig", "application/template", "application/main",  "esri/urlUtils"], function (templateOptions, Template, Main, urlUtils) {
          urlUtils.addProxyRule({
            urlPrefix: "https://rtca.cnr.ncsu.edu:6443/arcgis/",
            proxyUrl: "http://rtca.cnr.ncsu.edu/DotNet/proxy.ashx"
            });// start template
            var myTemplate = new Template(templateOptions);
            // create my main application. Start placing your logic in the main.js file.
            var myApp = new Main();
            // create my main application. Start placing your logic in the main.js file.

            myTemplate.startup().then(function (config) {
                //The config object contains the following properties: helper services, (optionally)
                //i18n, appid, webmap and any custom values defined by the application.
                //In this example we have one called theme.
                var appResponse = config.appResponse;
                if(config.appResponse){
                  delete config.appResponse;
                }
                if (config.edit && config.appid) {
                    // get the app builder code
                    require(["application/builder/builder"], function (builderMode) {
                        // create configuration app builder
                        var builder = new builderMode(config, appResponse);
                        // start it
                        builder.startup().otherwise(function (error) {
                            // something went wrong. Let's report it.
                            myApp.reportError(error);
                        });
                    });
                } else {
                    // lets go!
                    myApp.startup(config, appResponse);
                }
            }, function (error) {
                // something went wrong. Let's report it.
                myApp.reportError(error);

            });
        });
    </script>
    <!-- Google Analytics -->
    <script type="text/javascript">
        var _gaq = _gaq || [];
        _gaq.push(['_setAccount', 'UA-215788-4']);
         //_gaq.push(['_setDomainName', 'esri.com']);
        _gaq.push(['_trackPageview']);
        _gaq.push(['_trackPageLoadTime']);
        (function () {
            var ga = document.createElement('script');
            ga.type = 'text/javascript';
            ga.async = true;
            ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
            var s = document.getElementsByTagName('script')[0];
            s.parentNode.insertBefore(ga, s);
        })();
    </script>
</body>

</html>
