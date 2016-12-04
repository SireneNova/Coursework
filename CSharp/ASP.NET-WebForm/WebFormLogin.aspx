
<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="login.aspx.cs" Inherits="WebForms101.login" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
    <div>
        <p><asp:Label ID="Label1" runat="server" Text="First Name"></asp:Label>
        &nbsp;
        <asp:TextBox ID="txtFirst" runat="server"></asp:TextBox></p>
        <p><asp:Label ID="Label2" runat="server" Text="Last Name"></asp:Label>
        &nbsp;
        <asp:TextBox ID="txtLast" runat="server"></asp:TextBox></p>
        <p><asp:Button ID="btnSubmit" runat="server" Text="Login" OnClick="btnSubmit_Click"/></p>
        <p><asp:Label ID="lblName" BorderStyle="Inset" runat="server" Text=""></asp:Label></p>
    </div>
    </form>
</body>
</html>
