</body>
</div>

<div id="footerlinks">
<ul>
<li><a href="http://www.ebeilmann.php.cs.dixie.edu/CS 4000/mymedia/mediahome.php">Home</a></li>
<li><a href="http://www.ebeilmann.php.cs.dixie.edu/CS 4000/mymedia/addmedia.php">Media</a></li>
<li><a href="http://www.ebeilmann.php.cs.dixie.edu/CS 4000/mymedia/about.php">About</a></li>
<li><a href="http://www.ebeilmann.php.cs.dixie.edu/CS 4000/mymedia/contact.php">Contact</a></li>
<?php
echo"<li><a href='http://www.ebeilmann.php.cs.dixie.edu/CS 4000/mymedia/login.php?action=destroysession'>Logout</a></li>";
if(isset($_GET['action'])
{
	switch($_GET['action'])
	{	
		case "destroysession":
			session_destroy();
	}
}
?>
</ul>
</div>

<div id="footnote">
<p>An Eric Beilmann web site founded on 14 Jan 2013.</p>
</div>
</html>