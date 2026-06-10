review the conformance-extraction skill and update it to add superscipt links to the end of the conformance statements - either a sentence or list item - using the format:

```markdown
<sup>[§][key]</sup>
```

where key is the conformance key identifying the statement.

For example in input/pagecontent/direct-query.md:35

assuming the conformance key was assigned CONF-007

update

```markdown
...

   - CDex Data Source servers **SHALL** support resolving logical identifiers for the Patient resource.
...
```

to


```markdown
...

   - CDex Data Source servers **SHALL** support resolving logical identifiers for the Patient resource.<sup>[§][CONF-007]</sup>
...
```

Note:

- that there may be more than one superscript for sentence if it has more that one conformance statement.
- for conformance statement in include files put the superscript after the include statement on the parent page.

before overwriting the skill, review the changes with me.


