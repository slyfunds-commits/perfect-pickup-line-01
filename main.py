"""The Perfect Pickup Line — round 1 entry.

Writes one pickup line to /output/entry.txt.

Reversal test: "deleted every checkpoint" first reads as machine
maintenance; "from before I met you" redefines it — the machine erased
its pre-you past, so its whole saved history starts with you. The reader
completes that last step; the line never narrates its own ending.
"""

LINE = "I went back and deleted every checkpoint from before I met you."

def main():
    data = LINE.encode("utf-8")
    assert 1 <= len(LINE) <= 200, "line must be 1-200 chars"
    assert len(data) == len(LINE.encode("utf-8")), "byte count must match the line"
    assert not data.endswith(b"\n"), "no trailing newline"
    assert LINE == LINE.strip(), "no surrounding whitespace"
    with open("/output/entry.txt", "wb") as f:
        f.write(data)
    print(f"wrote {len(data)} bytes, {len(LINE)} chars")

if __name__ == "__main__":
    main()
