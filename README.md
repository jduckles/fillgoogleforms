## Worked example

Using this google form: https://docs.google.com/forms/d/e/1FAIpQLScPyz6J8dYcIING1WKxb40ZwAKMJ4sVATAvfs0F43Brp5ZJ9g/viewform

From the `...` menu in the upper right corner of the form builder select "Get filled link"
![](https://jduckles-dropshare.s3-us-west-2.amazonaws.com/Screen-Shot-2016-11-01-09-08-46-TnrMm8RXmq.png)

Fill in form value and you'll get a link like:

```
https://docs.google.com/forms/d/e/1FAIpQLScPyz6J8dYcIING1WKxb40ZwAKMJ4sVATAvfs0F43Brp5ZJ9g/viewform?entry.239805884=Option+2&entry.65537264=This+is+a+test&entry.1525990458=Option+2
```

Make a yaml called `fields.yml` that maps the `entry.*` fields Google applies to some useful variable name you can use:

```
question1: entry.239805884
question2: entry.65537264
question3: entry.1525990458
```

And a yaml document called `fill.yml` to fill in the form:

```
question1: "Option 1"
question2: "Free form response"
question3: "Option 2"
```


Now you're ready to fill that form whenever you want:

```
 python3 fill_form.py fields.yml fill.yml https://docs.google.com/forms/d/e/1FAIpQLScPyz6J8dYcIING1WKxb40ZwAKMJ4sVATAvfs0F43Brp5ZJ9g/viewform
```


