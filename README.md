# PyHTML
<h2>General Idea :</h2>
Implement HTML code using python, with giving the logic of programming - used in python - such that loops, conditions, variables ... etc.  
<h2>Fondation of the project :</h2>
<ul>
    <li>OOP in python.</li>
    <li>Relations between files, each one is as same important as the other one when we use the project.</li>
    <li>Two ways to implement and run the program</li>
</ul>
<h2>Different ways to implement :</h2>
<ol type='A'>
    <li>Using intrepting method, by runing "intrept.py" file.</li>
    <li>Store the code in variables, then using the function run (as you see in previews).</li>
</ol>
<h2>Steps to use each way :</h2>
<table>
    <tr>
        <th>With intrepting method :</th>
        <th>With variables :</th>
    <tr>
    <tr>
        <td>
            from oop import HTMLTags as t
        </td>
        <td>
            from oop import HTMLTags as t
            from oop import FileHandling as hf
        </td>
    </tr>
    <tr>
        <td>
            #start 
                < your code >
                (seperate between functions -that represent tags in html- with ';' )
            #end
        </td>
        <td>
            < variable name > = < PyHTML code >
        </td>
    </tr>
    <tr>
        <td>
            <b>In console :</b>
                python intrept.py 
                => write the FileName (without extension) you wanna extension.
                => enter '$stop$' to exit the console of PyHTMl.
        </td>
        <td>
            <b>In The end of file :</b>
            hf.run(VarNAme,"< file name >")
        </td>
    </tr>
</table>
<h2>The benifits of this project :</h2>
<ul>
    <li>Good way to create webpages using python for those who hate html :) </li>
    <li>In second way, you can use programming basics like conditions and loops to create the pages.</li>
    <li>Create many files in the same python file (see it in previews folder).</li>
    <li>Trying to edit on the code is good way that help you think better to solve problems and understand more the basics.</li>
</ul>
<q>
    <b>Note : </b>the project isn't ideal, there is many changes should be done on it, so I'll be so happy to see your pull requests on this GitHub repository.
</q>