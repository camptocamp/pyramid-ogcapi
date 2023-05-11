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
        href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.1.3/css/bootstrap.min.css"
        integrity="sha512-GQGU0fMMi238uA+a/bdWJfpUGKUkBdgfFdgBm72SUQ6BeyWjoY/ton0tEjH+OSH9iP4Dfh+7HM0I9f5eR0L/4w=="
        crossorigin="anonymous"
        referrerpolicy="no-referrer"
    />
    <title>${ title }</title>
    %if "description" in context.keys():
    <meta name="description" content="${ description }">
    %endif
  </head>
  <body>
    <div class="container-fluid">
      <h1>${ title }</h1>
      %if "description" in context.keys():
      <p>${ description }</p>
      %endif

      %for k in context.keys():
        <%
        v = context[k]
        %>
        %if k not in ("renderer_name", "caller", "title", "description", "links") and isinstance(v, (str, int, float, bool, list, dict)):
          <p><strong>${ k }</strong>: ${ v }</p>
        %endif
      %endfor

      %if "links" in context.keys() and links:
      <h3>Links</h3>
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
