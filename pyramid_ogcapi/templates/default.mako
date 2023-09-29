<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link
      rel="icon"
      type="image/png"
      sizes="32x32"
      href="https://geoservices-int.camptocamp.com/config/static/favicon-32x32.png"
      referrerpolicy="no-referrer"
    />
    <link
      rel="icon"
      type="image/png"
      sizes="16x16"
      href="https://geoservices-int.camptocamp.com/config/static/favicon-16x16.png"
      referrerpolicy="no-referrer"
    />
    <link
        rel="stylesheet"
        href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.2/css/bootstrap.min.css"
        integrity="sha512-b2QcS5SsA8tZodcDtGRELiGv5SaKSk1vDHDaQRda0htPYWZ6046lr3kJ5bAAQdpV2mmA/4v0wQF9MyU6/pDIAg=="
        crossorigin="anonymous"
        referrerpolicy="no-referrer"
    />
    %if "title" in context.keys():
    <title>${ title  }</title>
    %endif
    %if "description" in context.keys():
    <meta name="description" content="${ description }">
    %endif
    <style>
      th {
        vertical-align: top;
      }
      table {
        border: var(--bs-border-width) solid var(--bs-border-color);
        border-radius: var(--bs-border-radius);
        border-collapse: inherit;
      }
    </style>
  </head>
  <body>
    <script>
      (() => {
        'use strict'
        if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
          document.documentElement.setAttribute('data-bs-theme', 'dark');
        }
      })()
    </script>
    <div class="container-fluid">
      %if "title" in context.keys():
      <h1>${ title }</h1>
      %endif
      %if "description" in context.keys():
      <p>${ description }</p>
      %endif

      <%
      from pyramid_ogcapi.json2html import convert
      %>

      <%
      values = {}
      for k in context.keys():
          v = context[k]
          if k not in ("renderer_name", "caller", "title", "description", "links", "collections") and isinstance(v, (str, int, float, bool, list, dict)):
              values[k] = v

      html_values = convert(values)
      %>
      ${ html_values | n }

      %if "collections" in context.keys():
      <h2>Collections</h2>
      %for collection in collections:
        %if "title" in collection.keys():
        <h3>${ collection["title"] }</h3>
        %endif
        %if "description" in collection.keys():
        <p>${ collection["description"] }</p>
        %endif
        <%
        values = {}
        for k, v in collection.items():
            if k not in ("title", "description", "links"):
                values[k] = v

        html_values = convert(values, ["bbox", "interval"])
        %>
        ${ html_values | n }

        %if "links" in collection and collection["links"]:
        <h4>Links</h4>
        <ul class="list-group">
            %for link in collection["links"]:
            <li class="list-group-item">
                <a href="${ link["href"] }">${ link["title"] }</a>
            </li>
            %endfor
        </ul>
        %endif
      %endfor
      %endif

      %if "links" in context.keys() and links:
      <h2>Links</h2>
      <ul class="list-group">
        %for link in links:
          <li class="list-group-item">
            <a href="${ link["href"] }">${ link["title"] }</a>
          </li>
        %endfor
      </ul>
      %endif
    </div>
  </body>
</html>
