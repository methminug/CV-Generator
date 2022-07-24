# CV-Generator 🖨️
A python script that converts data in <b>JSON files to a .tex format</b> for a [LaTex CV template](https://github.com/posquit0/Awesome-CV), run automatically by a GitHub Actions workflow that also converts the generated .tex file to a CV in PDF format when changes are pushed to the ```master``` branch.

## But why? 🤔
LaTex templates are great for creating well formatted documents. <br/>
However, some may find it hard to work with the TeX type setting system used in LaTex, and may even feel that its not worth the time spent editing a complex looking .tex file to create a fairly simple looking CV.

And, that's what this script tries to fix.

## Usage
A user <b> edits the simple JSON files </b> in the ```sections``` folder that correspond to each section in the CV template. <br/>
Here's an example from the ```experience.json``` file for the Work Experience section of the CV.
```
{
    "title":"Work Experience",
    "sectionname":"cventries",
    "tagname":"cventry",
    "records":[
        {
            "title":"Software Engineer",
            "organization":"ABC Company",
            "location":"Mountain View, CA",
            "dates":"May 2020 - Present",
            "tasks-done":[
                "Lorem ipsum dolor sit amet.",
                "Elementum sagittis vitae et leo duis ut diam."
            ]
        },
        ...
        More records
        ...
    ]
}
```
<br/>

The values for ```title``` and ```records``` can be changed to reflect the user's data, while ```sectionname``` and ```tagname``` are for generating the layout for the .tex file.

Next, push the changes to the ```master``` branch and view the CV generated as a PDF in the ```generatedpdf``` folder.

## The template ✨
Awesome CV by posquit0 is the LaTex template used for this CV, and can be found at:<br/>
https://github.com/posquit0/Awesome-CV

Thank you for this cool template!

## Final thoughts
While this template isn't very complicated, I thought it might be fun to try and make editing it even more simple and take it a step further by automatically creating the PDF version as well.<br/>
So although this script may not save me a lot of time in the future, it was definitely fun to do. 😊<br/>
