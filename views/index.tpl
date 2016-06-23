<html>
<head>
    <title>NodeBasedRPGMapGenerator</title>
</head>

<body>
<script type="text/vnd.graphviz" id="graph">
    {{dot}}
</script>

<script src="http://mdaines.github.io/viz.js/viz.js"></script>

<center><div id="graph"></div></center>

<script>
    function inspect(s) {
        return "<pre>" + s.replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/\"/g, "&quot;") + "</pre>"
      }

      function src(id) {
        return document.getElementById(id).innerHTML;
      }

      function example(id, format, engine) {
        var result;
        try {
          result = Viz(src(id), format, engine);
          if (format === "svg")
            return result;
          else
            return inspect(result);
        } catch(e) {
          return inspect(e.toString());
        }
      }

      document.getElementById("graph").innerHTML = example("graph", "svg", "neato");
</script>
</body>
</html>
