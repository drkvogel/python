
TL;DNR: write tests in unittest but pytest cli provides better output

`unittest` - built in [tdd/unittest/unittest.md](/tdd/unittest/unittest.md)
`doctest` - [tdd/doctest/doctest.md](/tdd/doctest/doctest.md)
  good for small scripts and for documenting for non-programmers e.g. scientists
`pytest` (was `py.test`) - looks like most popular [tdd/pytest/pytest.md](/tdd/pytest/pytest.md)
`tox` - [tdd/tox/tox.md](/tdd/tox/tox.md)
`nose` - abandoned, superseded by pytest [nose.md](nose.md)

[Episode #11: Advice on Getting Started With Testing in Python – The Real Python Podcast ](https://realpython.com/podcasts/rpp/11/)

[Python : Relative benefits of pytest, unittest, nose, and doctest – rohitschauhan ](http://www.rohitschauhan.com/index.php/2018/07/05/python-relative-benefits-of-pytest-unittest-nose-and-doctest/)

>pytest code is shorter and simpler. For instance, pytest does not require you to include all your test cases within unittest’s TestMethods class, and does not require you to include a main() function.

[Start Here - Python Testing ](https://pythontesting.net/start-here/)

[My reaction to "Is TDD Dead?" - Python Testing ](https://pythontesting.net/agile/is-tdd-dead/)
[TDD is dead. Long live testing. (DHH) ](https://dhh.dk/2014/tdd-is-dead-long-live-testing.html)
[Test-induced design damage (DHH) ](https://dhh.dk/2014/test-induced-design-damage.html)
[Slow database test fallacy (DHH) ](https://dhh.dk/2014/slow-database-test-fallacy.html)
[The New Methodology ](https://martinfowler.com/articles/newMethodology.html)
[Test & Code : Python Testing for Software Engineering: 6: Writing software is like nothing else ](https://testandcode.com/6)
[Python Testing with pytest: Simple, Rapid, Effective, and Scalable by Brian Okken  The Pragmatic Bookshelf ](https://pragprog.com/book/bopytest/python-testing-with-pytest)

>actuallyalys 3 years ago A lot of existing Python code uses `nose`, so I'd say yes. `pytest` has more, but not that much more. `unittest` is even more common, so I'd definitely include that.

>jyper 3 years ago Although I love `py.test` at work stuff has to work with `unittest` since extra dependencies require setup/politics. Im just happy I can at least use requests.

>`Pytest` is far and away the best one, but there is still a need for `unittest` (some people have a requirement of not using external libraries, not many - but they exist).

>`py.test` runs `nose` tests afaik... so unless you have a lot of `nose` plugins the move over should be trivial.

>I really dislike `unittest` because it's very hard to compose (mix) tests and especially test setups and teardown, and because of the syntactic overhead and difficult reuse if the system under test is nontrivial you end up with lots of complex, duplicated and fragile test setup. That's even more problematic if you have to deal with multiple lifetimes.
>`pytest`'s fixtures do have a somewhat higher learning curve, but they're just so much more comfortable and convenient than the `xUnit` style.

