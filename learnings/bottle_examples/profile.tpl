<html>
<head>
    <title>My personal Details</title>
</head>

<body>
    <table>
        <tr>
            <td>Name</td>
            <td>{{Name}}</td>
        </tr>
        <tr>
            <td>Interests</td>
            <td>
                <ul>
                    %for i in Interests:
                    <li>{{i}}</li>
                    %end
                </ul>
            </td>
        </tr>
    </table>

<form method="POST" action="/forminput">
    <input type="text" name="name"/>
    <input type="submit" value="SuBMit"/>
</form>
</body>

</html>