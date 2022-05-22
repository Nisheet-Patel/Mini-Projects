Imports System.IO

Public Class Form1
    Dim font_name As String = "Source Sans Pro"
    Dim todolist As New List(Of CheckBox)
    Dim Tremain As Integer = 0
    Dim Tdone As Integer = 0
    Dim file_name As String = "task_data.txt"

    Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        AddButton.BackColor = Color.FromArgb(0, 125, 212)
        Bremove_checked.BackColor = Color.FromArgb(0, 125, 212)
        Ball_clear.BackColor = Color.FromArgb(0, 125, 212)
        ProgressBar1.ForeColor = Color.FromArgb(0, 125, 212)

        task_panel.BackColor = Color.White
        Panel2.BackColor = Color.White
        Panel3.BackColor = Color.White

        MenuStrip1.BackColor = Color.White

    End Sub

    'update status
    Private Sub update_status()
        status.Text = String.Format("{0} of {1} tasks done", Tdone, Tremain)
        Try
            ProgressBar1.Value = (100 \ Tremain) * Tdone
        Catch ex As Exception  'Solve Divide By 0 Error
            ProgressBar1.Value = 0
        End Try
    End Sub

    'toggle Strickthrough
    Private Sub toggle_strikethrough(sender As Object, e As EventArgs)
        If sender.CheckState = CheckState.Checked Then
            sender.Font = New Font(font_name, sender.font.size, FontStyle.Strikeout)

            'Status value Update 
            Tdone = Tdone + 1
        Else
            sender.Font = New Font(font_name, sender.font.size, FontStyle.Regular)
            'Status value Update 
            Tdone = Tdone - 1
        End If

        update_status()
    End Sub

    'Add List
    Private Sub add_task(title As String, Optional checked As Boolean = False, Optional foropen As Boolean = False)
        Dim CB As New CheckBox
        CB.AutoSize = True
        CB.Padding = New Padding(8, 8, 0, 8)
        CB.BackColor = Color.FromArgb(0, 125, 212)
        CB.ForeColor = Color.White
        CB.Dock = DockStyle.Top
        CB.Text = title
        CB.Checked = checked
        ' Font
        CB.Font = New Font(font_name, 15, FontStyle.Regular)


        'Add Event handler
        AddHandler CB.CheckedChanged, AddressOf toggle_strikethrough

        If foropen Then
            toggle_strikethrough(CB, New EventArgs)
        End If

        'Status value Update 
        Tremain = Tremain + 1

        update_status()

        task_panel.Controls.Add(CB)

    End Sub

    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles AddButton.Click

        If input_box.Text = "" Then
            Exit Sub
        End If

        add_task(input_box.Text)

        ' clear text box
        input_box.Text = ""
    End Sub

    Private Sub Remove_Checked(sender As Object, e As EventArgs) Handles Bremove_checked.Click
        For Each CB As CheckBox In task_panel.Controls
            If CB.Checked = True Then
                todolist.Add(CB)
                Tremain = Tremain - 1
                Tdone = Tdone - 1
            End If
        Next

        For Each CB As CheckBox In todolist
            task_panel.Controls.Remove(CB)
        Next
        todolist.Clear()

        update_status()
    End Sub

    Private Sub All_clear(sender As Object, e As EventArgs) Handles Ball_clear.Click
        task_panel.Controls.Clear()

        Tremain = 0
        Tdone = 0
        update_status()
    End Sub

    Private Sub save_list(ByVal file_name As String)
        Dim wfile As StreamWriter = New StreamWriter(Directory.GetCurrentDirectory() + "\" + file_name)
        Dim state As String

        For Each CB As CheckBox In task_panel.Controls
            If CB.Checked = True Then
                state = "1 "
            Else
                state = "0 "
            End If
            wfile.WriteLine(state + CB.Text)
        Next
        wfile.Close()

    End Sub

    Private Sub open_list(ByVal file_name As String)
        All_clear(New Object, New EventArgs)

        Dim rfile As StreamReader = New StreamReader(Directory.GetCurrentDirectory() + "\" + file_name)
        Dim line As String = rfile.ReadLine()

        While (line <> Nothing)
            If line.Substring(0, 1) = "1" Then
                add_task(line.Substring(1, Len(line) - 1), True, True)
            Else
                add_task(line.Substring(1, Len(line) - 1))
            End If
            line = rfile.ReadLine()
        End While

        rfile.Close()
    End Sub

    Private Sub SaveToolStripMenuItem_Click(sender As Object, e As EventArgs) Handles SaveToolStripMenuItem.Click
        save_list(file_name)
    End Sub

    Private Sub OpenToolStripMenuItem_Click(sender As Object, e As EventArgs) Handles OpenToolStripMenuItem.Click
        open_list(file_name)
    End Sub

End Class
