<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class Form1
    Inherits System.Windows.Forms.Form

    'Form overrides dispose to clean up the component list.
    <System.Diagnostics.DebuggerNonUserCode()> _
    Protected Overrides Sub Dispose(ByVal disposing As Boolean)
        Try
            If disposing AndAlso components IsNot Nothing Then
                components.Dispose()
            End If
        Finally
            MyBase.Dispose(disposing)
        End Try
    End Sub

    'Required by the Windows Form Designer
    Private components As System.ComponentModel.IContainer

    'NOTE: The following procedure is required by the Windows Form Designer
    'It can be modified using the Windows Form Designer.  
    'Do not modify it using the code editor.
    <System.Diagnostics.DebuggerStepThrough()> _
    Private Sub InitializeComponent()
        Dim resources As System.ComponentModel.ComponentResourceManager = New System.ComponentModel.ComponentResourceManager(GetType(Form1))
        Me.Panel2 = New System.Windows.Forms.Panel()
        Me.input_box = New System.Windows.Forms.TextBox()
        Me.AddButton = New System.Windows.Forms.Button()
        Me.MenuStrip1 = New System.Windows.Forms.MenuStrip()
        Me.SaveToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
        Me.OpenToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
        Me.Panel3 = New System.Windows.Forms.Panel()
        Me.status = New System.Windows.Forms.Label()
        Me.Ball_clear = New System.Windows.Forms.Button()
        Me.Bremove_checked = New System.Windows.Forms.Button()
        Me.ProgressBar1 = New System.Windows.Forms.ProgressBar()
        Me.task_panel = New System.Windows.Forms.Panel()
        Me.Panel2.SuspendLayout()
        Me.MenuStrip1.SuspendLayout()
        Me.Panel3.SuspendLayout()
        Me.SuspendLayout()
        '
        'Panel2
        '
        Me.Panel2.Controls.Add(Me.input_box)
        Me.Panel2.Controls.Add(Me.AddButton)
        Me.Panel2.Controls.Add(Me.MenuStrip1)
        Me.Panel2.Dock = System.Windows.Forms.DockStyle.Top
        Me.Panel2.Location = New System.Drawing.Point(0, 0)
        Me.Panel2.Name = "Panel2"
        Me.Panel2.Size = New System.Drawing.Size(396, 88)
        Me.Panel2.TabIndex = 1
        '
        'input_box
        '
        Me.input_box.Font = New System.Drawing.Font("Source Sans Pro", 18.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.input_box.Location = New System.Drawing.Point(12, 40)
        Me.input_box.Name = "input_box"
        Me.input_box.Size = New System.Drawing.Size(329, 38)
        Me.input_box.TabIndex = 2
        '
        'AddButton
        '
        Me.AddButton.FlatAppearance.BorderSize = 0
        Me.AddButton.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        Me.AddButton.Font = New System.Drawing.Font("Microsoft Sans Serif", 15.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.AddButton.ForeColor = System.Drawing.SystemColors.ControlLightLight
        Me.AddButton.Location = New System.Drawing.Point(347, 40)
        Me.AddButton.Name = "AddButton"
        Me.AddButton.Size = New System.Drawing.Size(37, 37)
        Me.AddButton.TabIndex = 3
        Me.AddButton.Text = "+"
        Me.AddButton.UseVisualStyleBackColor = True
        '
        'MenuStrip1
        '
        Me.MenuStrip1.Items.AddRange(New System.Windows.Forms.ToolStripItem() {Me.SaveToolStripMenuItem, Me.OpenToolStripMenuItem})
        Me.MenuStrip1.Location = New System.Drawing.Point(0, 0)
        Me.MenuStrip1.Name = "MenuStrip1"
        Me.MenuStrip1.Size = New System.Drawing.Size(396, 24)
        Me.MenuStrip1.TabIndex = 4
        Me.MenuStrip1.Text = "MenuStrip1"
        '
        'SaveToolStripMenuItem
        '
        Me.SaveToolStripMenuItem.Name = "SaveToolStripMenuItem"
        Me.SaveToolStripMenuItem.Size = New System.Drawing.Size(43, 20)
        Me.SaveToolStripMenuItem.Text = "Save"
        '
        'OpenToolStripMenuItem
        '
        Me.OpenToolStripMenuItem.Name = "OpenToolStripMenuItem"
        Me.OpenToolStripMenuItem.Size = New System.Drawing.Size(48, 20)
        Me.OpenToolStripMenuItem.Text = "Open"
        '
        'Panel3
        '
        Me.Panel3.Controls.Add(Me.status)
        Me.Panel3.Controls.Add(Me.Ball_clear)
        Me.Panel3.Controls.Add(Me.Bremove_checked)
        Me.Panel3.Controls.Add(Me.ProgressBar1)
        Me.Panel3.Dock = System.Windows.Forms.DockStyle.Bottom
        Me.Panel3.Location = New System.Drawing.Point(0, 417)
        Me.Panel3.Name = "Panel3"
        Me.Panel3.Size = New System.Drawing.Size(396, 44)
        Me.Panel3.TabIndex = 0
        '
        'status
        '
        Me.status.Location = New System.Drawing.Point(138, 9)
        Me.status.Margin = New System.Windows.Forms.Padding(5, 0, 5, 0)
        Me.status.Name = "status"
        Me.status.Size = New System.Drawing.Size(174, 23)
        Me.status.TabIndex = 2
        Me.status.Text = "0 of 1 tasks done"
        Me.status.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        '
        'Ball_clear
        '
        Me.Ball_clear.AutoSize = True
        Me.Ball_clear.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        Me.Ball_clear.ForeColor = System.Drawing.SystemColors.ControlLightLight
        Me.Ball_clear.Location = New System.Drawing.Point(318, 3)
        Me.Ball_clear.Name = "Ball_clear"
        Me.Ball_clear.Padding = New System.Windows.Forms.Padding(0, 5, 0, 5)
        Me.Ball_clear.Size = New System.Drawing.Size(66, 35)
        Me.Ball_clear.TabIndex = 1
        Me.Ball_clear.Text = "All Clear"
        Me.Ball_clear.UseVisualStyleBackColor = True
        '
        'Bremove_checked
        '
        Me.Bremove_checked.AutoSize = True
        Me.Bremove_checked.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        Me.Bremove_checked.ForeColor = System.Drawing.SystemColors.ControlLightLight
        Me.Bremove_checked.Location = New System.Drawing.Point(10, 2)
        Me.Bremove_checked.Name = "Bremove_checked"
        Me.Bremove_checked.Padding = New System.Windows.Forms.Padding(0, 5, 0, 5)
        Me.Bremove_checked.Size = New System.Drawing.Size(121, 35)
        Me.Bremove_checked.TabIndex = 0
        Me.Bremove_checked.Text = "Remove Checked   X"
        Me.Bremove_checked.UseVisualStyleBackColor = True
        '
        'ProgressBar1
        '
        Me.ProgressBar1.BackColor = System.Drawing.SystemColors.Control
        Me.ProgressBar1.Location = New System.Drawing.Point(138, 13)
        Me.ProgressBar1.Name = "ProgressBar1"
        Me.ProgressBar1.Size = New System.Drawing.Size(174, 23)
        Me.ProgressBar1.Step = 0
        Me.ProgressBar1.Style = System.Windows.Forms.ProgressBarStyle.Continuous
        Me.ProgressBar1.TabIndex = 0
        '
        'task_panel
        '
        Me.task_panel.AutoScroll = True
        Me.task_panel.BackColor = System.Drawing.SystemColors.Control
        Me.task_panel.Dock = System.Windows.Forms.DockStyle.Fill
        Me.task_panel.ForeColor = System.Drawing.SystemColors.ControlText
        Me.task_panel.Location = New System.Drawing.Point(0, 88)
        Me.task_panel.Name = "task_panel"
        Me.task_panel.Size = New System.Drawing.Size(396, 329)
        Me.task_panel.TabIndex = 2
        '
        'Form1
        '
        Me.AcceptButton = Me.AddButton
        Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.BackgroundImageLayout = System.Windows.Forms.ImageLayout.None
        Me.ClientSize = New System.Drawing.Size(396, 461)
        Me.Controls.Add(Me.task_panel)
        Me.Controls.Add(Me.Panel3)
        Me.Controls.Add(Me.Panel2)
        Me.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle
        Me.Icon = CType(resources.GetObject("$this.Icon"), System.Drawing.Icon)
        Me.MainMenuStrip = Me.MenuStrip1
        Me.MaximizeBox = False
        Me.MaximumSize = New System.Drawing.Size(412, 500)
        Me.MinimumSize = New System.Drawing.Size(412, 500)
        Me.Name = "Form1"
        Me.StartPosition = System.Windows.Forms.FormStartPosition.CenterParent
        Me.Text = "ToDo List | Nisheet"
        Me.Panel2.ResumeLayout(False)
        Me.Panel2.PerformLayout()
        Me.MenuStrip1.ResumeLayout(False)
        Me.MenuStrip1.PerformLayout()
        Me.Panel3.ResumeLayout(False)
        Me.Panel3.PerformLayout()
        Me.ResumeLayout(False)

    End Sub
    Friend WithEvents Panel2 As System.Windows.Forms.Panel
    Friend WithEvents input_box As System.Windows.Forms.TextBox
    Friend WithEvents AddButton As System.Windows.Forms.Button
    Friend WithEvents Panel3 As System.Windows.Forms.Panel
    Friend WithEvents task_panel As System.Windows.Forms.Panel
    Friend WithEvents MenuStrip1 As System.Windows.Forms.MenuStrip
    Friend WithEvents SaveToolStripMenuItem As System.Windows.Forms.ToolStripMenuItem
    Friend WithEvents status As System.Windows.Forms.Label
    Friend WithEvents Ball_clear As System.Windows.Forms.Button
    Friend WithEvents Bremove_checked As System.Windows.Forms.Button
    Friend WithEvents OpenToolStripMenuItem As System.Windows.Forms.ToolStripMenuItem
    Friend WithEvents ProgressBar1 As System.Windows.Forms.ProgressBar

End Class
