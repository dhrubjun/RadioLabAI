---
source_id: sdr_book_ch01_intro
source_category: curated_project_knowledge
title: What Is Software Defined Radio?
source_repository: dhrubjun/sdr-with-gnu-radio
source_path: book/01-what-is-software-defined-radio.md
sections: 1.1-1.3
---

# Chapter 1: What Is Software Defined Radio?

## 1.1 What Does a Radio Actually Do?

Before talking about Software Defined Radio, let's forget the word *software* for a moment and start with a simpler question:

> What does a radio actually do?

Suppose you want to listen to an FM radio station. The antenna on your radio is not receiving only that station. Many electromagnetic signals may be reaching it at the same time: other FM stations, mobile networks, Wi-Fi, Bluetooth, satellite signals and much more.

Yet when you tune the radio, you hear the station you selected.

Somewhere inside the receiver, a sequence of operations is separating the signal you want from everything else and recovering the information carried by it.

At a very high level, we can picture the process like this:

```text
Signal in the air
        ↓
Receive the signal
        ↓
Select the signal we want
        ↓
Remove what we do not want
        ↓
Recover the information
        ↓
Audio / Data / Image / Something useful
```

Of course, a real receiver is more complicated than this. But this simple picture already tells us something useful: a radio is essentially a chain of operations performed on a signal.

What changes with Software Defined Radio is not necessarily *what* we need to do to the signal. The interesting change is **where and how we perform those operations**.

---

## 1.2 The Traditional Way of Building a Radio

Traditionally, many radio operations have been carried out using dedicated electronic circuits.

A receiver might contain amplifiers, filters, mixers, oscillators and demodulators, with each part designed to perform a particular job.

A very simplified receiver could look something like this:

```text
Antenna
   ↓
RF Amplifier
   ↓
Analog Filter
   ↓
Mixer
   ↓
Another Filter
   ↓
Demodulator
   ↓
Audio
```

There is nothing inherently wrong with this approach. In fact, as we will soon see, SDR does not make analog hardware disappear.

The difference is flexibility.

Imagine that a particular part of a radio has been built specifically to process one kind of signal. If we later want the radio to behave differently, we may need to modify or replace some of that hardware.

Now imagine moving some of those operations into software.

Instead of changing a circuit, we could change an algorithm.

That is the idea that makes Software Defined Radio so interesting.

---

## 1.3 So What Is Software Defined Radio?

A **Software Defined Radio**, usually shortened to **SDR**, is a radio in which many of the signal-processing operations are performed digitally in software rather than being fixed entirely in dedicated hardware.

A simplified SDR receiver can be thought of as:

```text
Antenna
   ↓
RF Front End
   ↓
ADC
   ↓
Digital Samples
   ↓
Software Processing
   ↓
Information
```

The **ADC**, or **Analog-to-Digital Converter**, marks an important boundary.

Before the ADC, we are dealing with an analog electrical signal.

After the ADC, the signal is represented by a sequence of numbers called **samples**.

Once we have numbers, we can process them digitally.

That digital processing can eventually include things such as filtering, frequency translation, demodulation, synchronization, decoding and signal detection.

We are going to encounter all of these later in the book. For now, the important idea is much simpler:

> In SDR, much of what the radio does to a signal can be controlled through digital processing and software.
