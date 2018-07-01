package main

import (
	"fmt"
)

func main() {
	var s Inside
	s = "asdf"
	o := &Outside{
		Inside: &s,
	}
	Consume(o)
}

type OuterX interface {
	Inner() string
	Outer() string
}

type Inside string

type Outside struct {
	*Inside
}

func (i *Inside) Inner() string {
	return string(*i)
}

func (o *Outside) Outer() string {
	return fmt.Sprintf("%s %s", o.Inner(), o.Inner())
}

func Consume(o OuterX) {
	fmt.Println(o.Inner())
	fmt.Println(o.Outer())
}
